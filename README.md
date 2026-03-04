# OHS-YOLO-DETR

## Overview
OHS-YOLO-DETR is a lightweight and high-performance fabric defect detection algorithm integrating YOLOv8n and RT-DETR. It is specifically designed to address the trade-off between precision and computational efficiency for Automated Optical Inspection on resource-constrained edge devices.

## Key Features
* **Orthogonal Channel Attention (OCA):** Suppresses complex repetitive background noise and enhances feature discriminability by enforcing channel orthogonality.
* **Haar Wavelet Downsampling (HWD):** Replaces traditional pooling to preserve critical high-frequency defect details while reducing spatial redundancy and parameter count.
* **Semantics and Detail Infusion (SDI):** Hierarchically fuses multi-level feature maps to effectively handle extreme size imbalances across different defect categories.
* **Optimization:** Employs Focal-CIoU loss to improve bounding box regression accuracy for small defects, and utilizes offline knowledge distillation to significantly boost overall precision without adding inference overhead.

## Performance
Evaluated on complex industrial fabric datasets, OHS-YOLO-DETR achieves a mAP@0.5 of 41.7% and operates at a high speed of 220.6 FPS. It successfully condenses the architecture to only 5.78M parameters and 11.0 GFLOPs, providing an optimal Pareto balance for real-time edge deployment.






