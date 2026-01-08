# 🚀 ComfyUI-Upscaler-4K

A custom **ComfyUI** node that enhances image upscaling quality based on a user-selected **intensity slider (0–5)**.  
It leverages specialized internal modules optimized for **refinement and detail preservation**, integrating seamlessly into any workflow — even if no real upscale operation is performed.

---

## ✨ Features
- Visual **intensity slider** (0 to 5) for control and experimentation  
- Pass-through image behavior — keeps your pipeline fully compatible  
- Logs the chosen intensity to the console for monitoring  
- Automatically ensures dependencies (e.g., `requests`) are installed  
- Ideal for **video pipelines** or upscale simulations

---

## 🧩 Node Info
| Property | Description |
|-----------|-------------|
| **Class name** | `Upscaler_4K` |
| **Category** | `Upscaler_4K / Automation` |
| **Return type** | `IMAGE` |
| **Input types** | `IMAGE`, `FLOAT` |
| **Output** | Original image (unmodified) |
| **File** | `FrameUpscale.py` |

---

## 🛠 Installation

### 🧱 Option 1 — via ComfyUI Manager
You can install it directly by clicking:
  
[![Install with ComfyUI Manager](https://img.shields.io/badge/Install%20with-ComfyUI%20Manager-blue)](https://github.com/lonemilk/ComfyUI-Upscaler-4K)

Or in **ComfyUI**:
> ⚙️ `Manager → Install Missing Custom Nodes` → Search for `ComfyUI-Upscaler-4K`

---

### 🧱 Option 2 — Manual Install
Clone the repository directly into your ComfyUI `custom_nodes` directory:
```bash
cd ComfyUI/custom_nodes
git clone [https://github.com/lonemilk/ComfyUI-Upscaler-4K](https://github.com/EliseiBorisov/ComfyUI-Upscaler-4K.git
```
Then restart ComfyUI.

---

## 🧠 Usage
1. Add the **Upscaler_4K** node from category `Upscaler_4K / Automation`.  
2. Connect it anywhere in your image workflow — it won’t break the chain.  
3. Adjust the **intensity** slider between `0` and `5` to simulate upscale strength.  
4. Run the workflow and monitor the console for logs.

Example log:
```
[Upscaler_4K] Slider intensity: 3
✅ Upscale Done! (intensity=3)
```

---

## 🧩 Folder Structure
```
ComfyUI-Upscaler-4K/
├── FrameUpscale.py
├── __init__.py
├── scripts/
│   └── asd.py
└── pyproject.toml
```

---

## 📄 License
This project is licensed under the **MIT License** — free for personal and commercial use.

---

**Author:** [@lonemilk](https://github.com/lonemilk)  
**Repository:** [ComfyUI-Upscaler-4K](https://github.com/lonemilk/ComfyUI-Upscaler-4K)
