# Empire State Building Detection
Computer Vision Assignment #2

**#1. Empire State Building  확인하기** 

#2 번을  수행한  이후  empire  레이블에  해당하는 bounding box 의  개수를  세서  0 개이면  False 를,  1 개면  True 를  출력하였다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.001.png) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.002.png) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.003.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.004.jpeg)![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.005.jpeg)

위  사진에  대한  출력  결과는  차례대로  아래와  같다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.006.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.007.jpeg)![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.008.jpeg)

위  사진에  대한  출력  결과는  아래와  같다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.009.png)

**#2. Empire State Building  위치찾기** 

Empire State Building 을  포함하는  이미지  데이터셋을  이용해  모델을  훈련시키기  위해  딥러닝  기반 객체  탐지  알고리즘  중, YOLOv5 를  사용하였다.  이는  실시간  객체  탐지  시스템으로,  이미지를  한 번만  보고  여러  객체를  탐지하고  분류할  수  있다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.010.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.011.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.012.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.013.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.014.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.015.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.016.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.017.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.018.jpeg)

잘  학습시켰다고  생각했지만  다른  빌딩도  empire  building 으로  인식하는  문제에  직면하였다. 검색해보니  레이블이  하나면  이런  경우가  발생한다고  하여,  명세서  참고자료에  있는  모든  빌딩들 약  10 개씩  데이터를  수집한  후  위  과정을  다시  진행하였다. 

아래는  학습시킨  이미지  파일들이다 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.019.jpeg) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.020.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.021.jpeg) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.022.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.023.jpeg) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.024.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.025.jpeg) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.026.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.027.jpeg)![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.028.jpeg)

레이블도  아래와  같이  추가해준다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.029.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.030.jpeg)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.031.png)

학습  횟수는  2000 번으로  설정하여  정확도를  높여주었다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.032.jpeg)

Empire state building 에  대한  출력  결과는  아래와  같다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.033.png) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.034.png) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.035.png)

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.036.jpeg) ![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.037.jpeg)

Empire state building 이  아닌  사진들에  대한  출력  결과는  아래와  같다. 

![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.038.jpeg)![](/src/Aspose.Words.8abd1d53-732c-4f80-956c-905a26d702d1.039.jpeg)
