

# 📖 Storyboard Generator using OpenAI API

## 📝 **Objective**

Transform a short narrative story into a structured **10-scene visual storyboard**, where each scene includes:

* A brief **storyline (1–2 sentences)**.
* A representative **image URL** (generated using DALL·E via OpenAI API).

---

## 🚀 **Features**

* 🧠 Uses **GPT-4** to break the story into 10 progressive scenes.
* 🎨 Generates **scene-specific images** using **DALL·E**.
* 📦 Outputs the complete storyboard as a well-structured **JSON file**.
* ✅ Optional fallback for image generation errors.
* 💡 No UI included — backend-only solution.

---

## 📂 **Project Structure**

```
storyboard-generator/
│
├── generate_storyboard.py          # Main Python script
├── storyboard_with_images.json     # Output JSON with scenes & images
├── requirements.txt                # Required Python packages
├── .env                            # OpenAI API Key (environment variable)
└── README.md                       # Project documentation
```

---

## ⚙️ **Setup Instructions**

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/storyboard-generator.git
   cd storyboard-generator
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**:
   Create a `.env` file:

   ```bash
   OPENAI_API_KEY=your-openai-api-key-here
   ```

4. **Run the script**:

   ```bash
   python generate_storyboard.py
   ```

---

## 📤 **Output**

* Generates `storyboard_with_images.json` in the following format:

```json
[
  {
    "scene_number": 1,
    "storyline": "A young boy builds a robot in his garage using scrap parts.",
    "image_prompt": "A boy assembling a robot from metal parts in a messy garage.",
    "image_url": "https://openai-generated-image-url.com/scene1.jpg"
  },
  ...
]
```

---

## ❗ **Note**

* Requires an active **OpenAI API Key** with **Chat API** and **DALL·E access**.
* If image generation fails, a fallback URL is assigned.

---





