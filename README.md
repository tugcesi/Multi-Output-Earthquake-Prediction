# Multi-Output Earthquake Prediction

Bu repo, makine öğrenmesi ve derin öğrenme ile depremin büyüklüğü (**Magnitude**) ve derinliğini (**Depth**) tahmin etme projesidir.

## Kurulum

Gerekli paketleri yükleyin:

```
pip install -r requirements.txt
```

## Streamlit Arayüzü

Ana dizinde şu komutu çalıştırın:

```
streamlit run streamlit_app.py
```

Gerekli parametreleri girin ve **Tahmin Et** butonuna tıklayın.

> **Not:** Model dosyanızın (`earthquake_pred.joblib` veya `earthquake_pred.pkl`) ana dizinde olması gerekir.