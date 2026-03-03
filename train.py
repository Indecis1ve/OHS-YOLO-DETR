import warnings
warnings.filterwarnings('ignore')
from ultralytics import RTDETR

# 深度学习炼丹必备必看必须知道的小技巧！https://www.bilibili.com/video/BV1q3SZYsExc/
# 整合多个创新点的B站视频链接:https://www.bilibili.com/video/BV15H4y1Y7a2/
# 更多问题解答请看使用说明.md下方<常见疑问>

if __name__ == '__main__':
    # model = RTDETR('ultralytics/cfg/models/rt-detr/rtdetr-r18.yaml')
    # model.load('') # loading pretrain weights
    model = RTDETR('ultralytics/cfg/models/yolo-detr/yolov8-detr-HWD.yaml')
    model.train(
                # data='dataset1/data.yaml',
                data='TILDA/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=4,
                workers=8,# Windows下出现莫名其妙卡主的情况可以尝试把workers设置为0
                # device='0', # 指定显卡和多卡训练问题 统一都在<使用说明.md>下方常见错误和解决方案。
                # resume='', # last.pt path
                # resume='runs/train/exp20/weights/last.pt',
                project='runs/train',
                name='exp',
                )