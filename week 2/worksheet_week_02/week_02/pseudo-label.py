import random
import torch
import torchvision
from torch import nn
import torch.nn.functional as F
from torchvision import transforms
import PIL.ImageOps
from PIL import Image, ImageFilter
from torch.utils.data import DataLoader
import modules
import time
import matplotlib.pyplot as plt  
import os  
import PIL.ImageOps
from PIL import Image
from PIL import ImageFile
from datetime import datetime

def evaluate_dataset(dataloader, net, criterion, device, threshold_pneumonia=0, save=False, Pneumonia_root='', Unknown_root=''):
    """
    评估数据集并根据阈值分类为pneumonia或unknown
    """
    mses = []
    total = 0
    pneumonia = 0
    unknown = 0
    net.eval()
    to_Image = torchvision.transforms.ToPILImage()
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    with torch.no_grad():
        counter = 0
        for inputs, target, origin in dataloader:
            inputs, target = inputs.to(device), target.to(device)
            outputs = net(inputs)
            loss = criterion(outputs, target)
            mses.append(loss.item())
            total += 1
            
            if save:
                img_pil = to_Image(origin.squeeze(0).cpu())
                counter += 1
                filename = f"{timestamp}_{counter}.png"
                
                # 只分为pneumonia和unknown两类
                if loss.item() > threshold_pneumonia:
                    pneumonia += 1
                    filepath = os.path.join(Pneumonia_root, filename)
                    img_pil.save(filepath)
                    print(f"Saved as pneumonia: {filename}, Loss: {loss.item():.4f}")
                else:
                    unknown += 1
                    filepath = os.path.join(Unknown_root, filename)
                    img_pil.save(filepath)
                    print(f"Saved as unknown: {filename}, Loss: {loss.item():.4f}")
    
    return mses, total, pneumonia, unknown

def compute_top_percent(maes, percent=0.01):
    sorted_mses = sorted(maes, reverse=True)
    k = max(1, int(len(sorted_mses) * percent))
    return sum(sorted_mses[:k]) / k

def Only_evaluate_dataset(dataloader, net, criterion, device):
    """
    仅评估数据集，返回loss列表
    """
    maes = []
    net.eval()
    with torch.no_grad():
        for inputs, target in dataloader:
            inputs, target = inputs.to(device), target.to(device)
            outputs = net(inputs)
            loss = criterion(outputs, target)
            maes.append(loss.item())
    return maes

def main():
    
    os.makedirs("loss_plots", exist_ok=True)
    os.makedirs("reconstruction_comparisons", exist_ok=True)
    
    ImageFile.LOAD_TRUNCATED_IMAGES = True
    
    # 创建锐化滤波器
    sharpen_kernel = ImageFilter.UnsharpMask(radius=1, percent=150, threshold=3)
    
    # 定义锐化变换
    class SharpenTransform:
        def __call__(self, img):
            return img.filter(sharpen_kernel)
    
    # 应用锐化和高斯噪声的变换
    transform = transforms.Compose([
        SharpenTransform(),  # 先锐化
        modules.AddGaussianNoise(amplitude=51),
        transforms.Resize([512, 512]),  # 调整为512x512
        transforms.ToTensor(),
    ])
    
    # 基准数据集用于确定阈值（使用正常样本）
    Test_Dataset = modules.DUAE_Dataset(
        root_dir="archive/chest_xray/chest_xray/train/NORMAL",
        transform=transform,
        should_invert=False,
        n=500,
        noice_amplitude=26
    )
    Test_dataloader = DataLoader(
        Test_Dataset, 
        shuffle=True, 
        batch_size=1,
        pin_memory=True
    )
    
    # 待标记的数据集（可以是任何数据集）
    # 这里以混合数据集为例
    Target_Dataset = modules.DUAE_Lable_Dataset(
        root_dir="target_dataset_path",  # 替换为您要标记的数据集路径
        transform=transform,
        should_invert=False,
        n=1000,  # 根据实际数据量调整
        noice_amplitude=26
    )
    Target_dataloader = DataLoader(
        Target_Dataset, 
        shuffle=True, 
        batch_size=1,
        pin_memory=True
    )
    
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    net = modules.DarkUnet().to(device)
    criterion = nn.L1Loss()
    net.load_state_dict(torch.load('pth/model_final.pth'))
    net.eval()
    
    # 使用正常数据计算基准阈值
    print("Computing baseline threshold from normal samples...")
    test_losses = Only_evaluate_dataset(Test_dataloader, net, criterion, device)
    test_mean = sum(test_losses) / len(test_losses)
    test_var = sum((x - test_mean)**2 for x in test_losses) / len(test_losses)
    test_std = test_var ** 0.5
    
    # 可调整的阈值参数
    # 方法1: 基于统计的阈值
    threshold_multiplier = 2.5  # 可调整：1.5, 2.0, 2.5, 3.0
    THRESHOLD_PNEUMONIA = test_mean + threshold_multiplier * test_std
    
    # 方法2: 基于百分位数的阈值
    # threshold_percentile = 0.95  # 可调整：0.9, 0.95, 0.99
    # THRESHOLD_PNEUMONIA = sorted(test_losses)[int(len(test_losses) * threshold_percentile)]
    
    # 方法3: 固定阈值
    # THRESHOLD_PNEUMONIA = 0.1  # 可根据经验调整
    
    print(f"Baseline statistics:")
    print(f"Mean: {test_mean:.4f}")
    print(f"Std: {test_std:.4f}")
    print(f"Pneumonia threshold: {THRESHOLD_PNEUMONIA:.4f}")
    
    # 创建输出目录
    os.makedirs('Pseudo_Data/pneumonia', exist_ok=True)
    os.makedirs('Pseudo_Data/unknown', exist_ok=True)
    
    # 对目标数据集进行伪标签分类
    print("\nStarting pseudo-labeling...")
    target_losses, total, pneumonia_count, unknown_count = evaluate_dataset(
        Target_dataloader, 
        net, 
        criterion, 
        device, 
        THRESHOLD_PNEUMONIA, 
        save=True,  # 设置为True以保存图像
        Pneumonia_root='Pseudo_Data/pneumonia',
        Unknown_root='Pseudo_Data/unknown'
    )
    
    # 统计结果
    print(f"\nPseudo-labeling results:")
    print(f"Total samples: {total}")
    print(f"Pneumonia samples: {pneumonia_count} ({pneumonia_count/total*100:.1f}%)")
    print(f"Unknown samples: {unknown_count} ({unknown_count/total*100:.1f}%)")
    
    # 绘制loss分布图
    plt.figure(figsize=(12, 8))
    
    # 子图1: 基准数据和目标数据的loss分布
    plt.subplot(2, 1, 1)
    plt.hist(test_losses, bins=30, alpha=0.7, label='Baseline (Normal)', color='green', density=True)
    plt.hist(target_losses, bins=30, alpha=0.7, label='Target Dataset', color='blue', density=True)
    plt.axvline(x=THRESHOLD_PNEUMONIA, color='red', linestyle='--', linewidth=2, 
                label=f'Pneumonia Threshold ({THRESHOLD_PNEUMONIA:.4f})')
    plt.xlabel('L1 Loss (MAE)')
    plt.ylabel('Density')
    plt.title('Loss Distribution Comparison')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # 子图2: 伪标签分类结果
    plt.subplot(2, 1, 2)
    pneumonia_losses = [loss for loss in target_losses if loss > THRESHOLD_PNEUMONIA]
    unknown_losses = [loss for loss in target_losses if loss <= THRESHOLD_PNEUMONIA]
    
    if pneumonia_losses:
        plt.hist(pneumonia_losses, bins=20, alpha=0.8, label=f'Pneumonia ({len(pneumonia_losses)})', 
                color='red', density=True)
    if unknown_losses:
        plt.hist(unknown_losses, bins=20, alpha=0.8, label=f'Unknown ({len(unknown_losses)})', 
                color='gray', density=True)
    
    plt.axvline(x=THRESHOLD_PNEUMONIA, color='red', linestyle='--', linewidth=2, 
                label=f'Threshold ({THRESHOLD_PNEUMONIA:.4f})')
    plt.xlabel('L1 Loss (MAE)')
    plt.ylabel('Density')
    plt.title('Pseudo-labeling Results')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('pneumonia_pseudo_labeling_results.pdf')
    plt.savefig('pneumonia_pseudo_labeling_results.png', dpi=300)
    plt.close()
    
    print(f"\nResults saved:")
    print(f"- Distribution plot: pneumonia_pseudo_labeling_results.pdf")
    print(f"- Pneumonia samples: Pseudo_Data/pneumonia/")
    print(f"- Unknown samples: Pseudo_Data/unknown/")

if __name__ == "__main__":
    main()