# hand-keypoint-detect

直接在python中使用谷歌mediapipe的手关键点检测

直接调用电脑摄像头检测命令

    python detect_on_camera.py  


models文件夹中是检测用模型

data文件夹中存放的是anchors配置文件

gasture_utils是根据关键点设置一些规则进行手势分类，该方法不适用深度学习方式，可以在gasture_utils/determine_gastures.py自定义五根手指的指向弯曲程度设置新的手势

在电脑上检测效果没有mediapipe给的安卓apk效果好，应该是谷歌还用了一些别的方法进行优化，后面会持续优化更新,最终目标是做一个可靠的远距离手势检测来控制其他设备。



检测图像
![efficientd4](https://github.com/ndkjing/detection_keras_tf/blob/master/eval_infer/images_out/efficientdet4.png)



## 参考：

[检测模型](https://github.com/google/mediapipe)
