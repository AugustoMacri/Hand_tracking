# Hand Tracking

Este projeto utiliza **Visão Computacional com MediaPipe** e **OpenCV** para controlar o volume do sistema Linux com o movimento das mãos (polegar e indicador).

> Baseado no curso [Advanced Computer Vision with Python](https://www.youtube.com/watch?v=01sAkU_NvOY) do **freeCodeCamp.org**.

---

## Tecnologias Utilizadas

- [Python 3.10](https://www.python.org/)
- [OpenCV](https://opencv.org/)
- [MediaPipe](https://google.github.io/mediapipe/)
- [PulseAudio (pulsectl)](https://github.com/mk-fg/python-pulse-control) – controle de volume no Linux
- `requirements.txt` incluso com todas as dependências

---

## Como Rodar o Projeto

1. **Clone o repositório** e acesse a pasta:

```bash
git clone https://github.com/AugustoMacri/Hand_tracking
```

2. **Crie um ambiente virtual e ative-o**:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
# ou
venv\Scripts\activate     # Windows
```

3. **Instale as dependências**:

```bash
pip install -r requirements.txt
```

4. **Execute o projeto**:

```bash
python VolumeHandControl.py
```

> **Obs:** o script `HandTrackingModule.py` é importado como um módulo auxiliar para detecção de mãos.

---

## Estrutura do Projeto

```
Hand_tracking/
├── HandTrackingModule.py      # Módulo com a lógica de detecção de mãos
├── VolumeHandControl.py       # Script com controle de volume
├── requirements.txt           # Dependências do projeto
```


## Créditos

Este projeto foi desenvolvido com base no curso [Advanced Computer Vision with Python](https://www.youtube.com/watch?v=01sAkU_NvOY) da [freeCodeCamp.org](https://www.freecodecamp.org/).

---