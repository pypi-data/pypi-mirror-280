# AutoBlur

### 🛠 Tool
<img src="https://img.shields.io/badge/Python-3766AB?style=flat-square&logo=Python&logoColor=white"/> <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white"/> <img src="https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white"/> <img src="https://img.shields.io/badge/VSCode-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"/> <img src="https://img.shields.io/badge/tkinter-47A248?style=flat-square&logo=Python&logoColor=white"/> 

### 개발환경
💻 M1 Pro Mac (Sonoma)

## 프로젝트 소개

AutoBlur는 영상 편집의 편의와 영상에 나온 사람들의 초상권을 보호하는 프로그램입니다.

PyQt와 Yolov8을 사용하여 구현하였으며 사용 모델은 아래 레퍼지토리에서 사용했습니다.

- [yolov8-face🏠](https://github.com/akanametov/yolov8-face)

-> model 디렉터리에 모델을 다운로드해야 합니다. 


## 사용 방법

앱을 실행하면 이러한 창이 생깁니다.
<div align="center">
   <img src="image.png">

</div>
- Open Video는 사용자가 원하는 영상 파일을 열어 자동으로 얼굴을 인식하고, 모자이크 처리를 진행합니다. 

- DownLoad Video는 클릭 시 유튜브 링크를 입력하는 창이 나오고, 반환하면 저장할 위치를 입력 받고 영상을 저장합니다. ( 유튜브에서 다운로드를 할 수 없는 영상도 있으니 참고 바랍니다. )

- 앱을 실행하면 .temp 디렉터리와 BluredVideo가 생성되며, 프로그램의 결과물이 BluredVideo에 저장됩니다. .temp는 각 영상을 임시로 파일이 저장되었다가 소리가 합쳐진 다음 자동으로 삭제됩니다. ( 이 두 디렉터리는 앱 실행중에 삭제하면 안됩니다. )

<br>

```
git clone https://github.com/codernoah404/AutoBlur.git
```

사용중인 가상환경을 활성화한 후 라이브러리를 설치하고, 앱을 실행시킵니다.

```
pip install -r requirements.txt
python src/app.py
```
