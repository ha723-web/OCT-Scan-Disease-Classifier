# 👁️ OCT Scan Disease Classifier

A simple AI-powered web app that classifies **OCT retinal scans** into four categories: **CNV**, **DME**, **DRUSEN**, or **NORMAL**. Built using PyTorch and Streamlit, it's designed to help raise awareness and support early eye disease screening.

**LINK TO THE APP : https://oct-scan-disease-classifier.streamlit.app/** 

---

## 📖 What Is OCT and Why It Matters

**OCT (Optical Coherence Tomography)** is a non-invasive scan used by eye doctors to view layers of the retina. Diseases like:

* **CNV (Choroidal Neovascularization)**
* **DME (Diabetic Macular Edema)**
* **DRUSEN** (early sign of macular degeneration)

can lead to **vision loss**. Quick and accurate screening helps prevent serious damage. This tool shows how AI can assist in that process.

---

## 🧠 What This App Does

* 📤 Upload an OCT scan image (JPG or PNG)
* 🤖 The model predicts one of the four classes
* 🖼️ Displays the image with prediction result
* ✅ Simple UI built with Streamlit

---

## 🛠️ Technologies Used

* **Python** – Programming language
* **PyTorch** – Deep learning framework
* **Streamlit** – To build the web interface
* **Torchvision** – Image transformations
* **PIL (Pillow)** – Image handling

---

## 📁 Project Structure

```
oct-disease-classifier/
├── app.py                # Main Streamlit app
├── requirements.txt      # Required Python packages
├── model/
│   └── oct_model.pth     # Trained ResNet18 model
├── utils/
│   └── predict.py        # Prediction logic
├── uploads/              # Uploaded images folder
```

---

## ▶️ How to Run the Project (Mac/Terminal)

```bash
# Go to your project folder
cd ~/Desktop/oct-disease-classifier

# Set up virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at: **[http://localhost:8501](http://localhost:8501)**

---

## 📦 requirements.txt Content

```
torch
torchvision
streamlit
matplotlib
Pillow
```

---

## ⚠️ Disclaimer

This project is for **learning and research only**. It does **not replace medical diagnosis**. Always consult a certified doctor for health decisions.

---

## 👩‍⚕️ About Me

**Harshini Akunuri**
M.S. in Computer Science | AI in Healthcare Enthusiast
📧 [harshiniakunuri59@gmail.com](mailto:harshiniakunuri59@gmail.com)
🔗 [LinkedIn](https://www.linkedin.com/in/harshini-akunuri/)

---

## 🔮 Future Additions

* Add visual explanation (Grad-CAM)
* Improve accuracy with more training data
* Deploy online using Streamlit Cloud
* Generate PDF report

---

## 📚 Data Source

Trained on public OCT dataset from:
**Kermany et al. (2017)** – *Identifying Medical Diagnoses by Deep Learning*
[Read paper](https://doi.org/10.1016/j.cels.2018.02.010)

---

## 🧪 How I Trained the Model (OCT2017 Dataset)

This project uses the **OCT2017 retinal scan dataset** published by Kermany et al., which includes labeled images across 4 classes:

* **CNV** – Choroidal Neovascularization
* **DME** – Diabetic Macular Edema
* **DRUSEN** – Early signs of macular degeneration
* **NORMAL** – Healthy retina

### 🧑‍💻 Training Steps

1. **Dataset Structure:**

```
data/
├── train/
├── test/
└── val/
```

Each folder contains subfolders for CNV, DME, DRUSEN, and NORMAL classes with corresponding images.

2. **Model Used:**

* **ResNet18** from torchvision (pre-trained on ImageNet)
* Replaced the final fully connected layer with 4 output nodes

3. **Training Code:**
   The model was trained using:

* `torchvision.datasets.ImageFolder` to load images
* `torch.utils.data.DataLoader` for batching
* `CrossEntropyLoss` for classification
* `Adam` optimizer with a learning rate of 0.0003
* Trained for 5 epochs

```bash
# Run training script
python model/train_model.py
```

After training, the model was saved as:

```bash
model/oct_model.pth
```

4. **Training Duration:**

> \~4–5 hours on a Mac M1 (CPU) for \~2600 batches per epoch

---


