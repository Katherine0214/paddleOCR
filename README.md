# PaddleOCR
>本算法包用于实现文字检测、识别。

>此处提供的程序不全，完整程序见https://github.com/PaddlePaddle/PaddleOCR



### 🛠️ PaddleOCR环境配置
https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/quickstart.md


#### 进入本地配好环境（已安装好PaddlePaddle和PaddleOCR whl包）
运行```conda activate paddle_env```



### 一、目录文件说明
---
- ```doc文件夹```：用于存放测试图片；
- ```inference文件夹```：用于存放训练好的推理模型（需网上下载）；

   ⚡ PP-OCR模型推理库：
   https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/models_list.md
- ```tools\inference文件夹```：用于各种推理运行的代码，我一般把他复制到主目录下的test.py中（且需要添加一行代码：    ```os.environ["KMP_DUPLICATE_LIB_OK"]='TRUE'```）。




### 二、模型推理
---
官网：https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.6/doc/doc_ch/inference_ppocr.md

本地运行时记得添加```--use_gpu false```

- ### 📚 1、文本检测
   ```python tools/infer/predict_det.py --image_dir=待检测图片 --det_model_dir=加载的推理模型```

   检测结果默认保存到```./inference_results```文件夹里（包括可视化图片+位置txt文档）。

- ### 👫 2、文本识别
  （因为识别前必须先检测位置，而这里只进行识别，因此给的图片都是截取过的单个词条；如果多词条的识别详见（4）中）
  - #### a.  超轻量中文识别
     ```python tools/infer/predict_rec.py --image_dir=待检测图片 --rec_model_dir=加载的推理模型```

     识别结果（识别的文本和得分）会打印到屏幕上。

  - #### b.  英文识别
     ```python tools/infer/predict_rec.py --image_dir=待检测图片 --rec_model_dir=加载的推理模型 --rec_char_dict_path=对应语种的字典路径  "ppocr/utils/en_dict.txt"```

     识别结果（识别的文本和得分）会打印到屏幕上。

  - #### c.  多语言识别
     ```python tools/infer/predict_rec.py --image_dir=待检测图片 --rec_model_dir=加载的推理模型 --rec_char_dict_path=对应语种的字典路径  "ppocr/utils/dict/korean_dict.txt" --vis_font_path=对应语种的可视化的字体路径    "doc/fonts/korean.ttf"```

     识别结果（识别的文本和得分）会打印到屏幕上 。

- ### 📖 3、方向分类
   ```python tools/infer/predict_cls.py --image_dir=待检测图片 --cls_model_dir=加载的推理模型```

   预测结果（分类的方向和得分）会打印到屏幕上。

- ### 🔥 4、文本检测、方向分类和文字识别串联推理（重要）
  - #### a.  使用方向分类器
     ```python tools/infer/predict_system.py --image_dir=待检测图片 --det_model_dir=检测模型 -cls_model_dir=分类模型 --rec_model_dir=识别模型 --use_angle_cls=true（使用方向分类器）```

  - #### b.  不使用方向分类器
     ```python tools/infer/predict_system.py --image_dir=待检测图片 --det_model_dir=检测模型 --rec_model_dir=识别模型 -use_angle_cls=false（不使用方向分类器）```

  - #### c.  使用多进程
     ```python tools/infer/predict_system.py --image_dir=待检测图片 --det_model_dir=检测模型 --rec_model_dir=识别模型 -use_angle_cls=false（不使用方向分类器） --use_mp=True（使用多进程） --total_process_num=6```



### 👀 三、行程码识别实例
---
```python tools/infer/predict_system.py --image_dir="./doc/imgs/1.jpg" --det_model_dir="./inference/ch_PP-OCRv3_det_infer/" --cls_model_dir="./inference/ch_ppocr_mobile_v2.0_cls_infer/" --rec_model_dir="./inference/ch_PP-OCRv3_rec_infer/" --use_angle_cls=true --use_gpu=False```

检测结果默认保存到```./inference_results```文件夹里（包括可视化图片+位置and识别的system_results.txt文档）。






