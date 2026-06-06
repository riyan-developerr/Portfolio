# Marketing Video Generator V1

A local AI-assisted marketing video generator that turns a product image and product description into a short vertical ad video with scene planning, background removal, styled visual shots, motion polish, music/SFX, export options, and quality scoring.

This project is my MVP version: the system is intentionally built around a stable template-motion engine first, with future hooks for AI image-to-video tools such as ComfyUI or Diffusers.

---

## Demo Status

**MVP achieved:** Yes  
**Current output:** Short vertical MP4 product ad  
**Current backend:** Template motion engine using MoviePy/FFmpeg  
**Future backend support:** ComfyUI and Diffusers structure prepared but not enabled yet

Recommended demo settings:

```text
Style: luxury
Duration: 6-8 seconds
Output: MP4
Product image: clean product photo with plain background
```

---

## What the Project Does

The app accepts a product image and product details, then automatically:

1. Generates a marketing scene plan using a local Qwen model.
2. Removes the product background and prepares clean product assets.
3. Creates three designed ad scenes: hero, detail, and CTA.
4. Adds motion effects such as slow zoom, glow, particles, vignette, and light sweep.
5. Adds background music and optional transition sound effects.
6. Exports the final result as MP4, with optional GIF export.
7. Logs generation metadata and allows manual scoring for later analysis.

---

## Key Features

- Local LLM planning with `Qwen/Qwen3-0.6B`
- JSON-based scene planning
- Product background removal using `rembg`
- Template-based shot generation
- Style presets using `configs/styles.json`
- Vertical ad format: `1080 x 1920`
- Music and optional SFX support
- MP4 export and optional GIF export
- Gradio web UI
- Run logging in `data/runs.csv`
- Manual scoring system for evaluating output quality
- Future-ready backend structure for ComfyUI and Diffusers

---

## Tech Stack

| Area | Tools |
|---|---|
| UI | Gradio |
| LLM planning | Hugging Face Transformers, Qwen3-0.6B |
| Image processing | Pillow, OpenCV, rembg, onnxruntime |
| Video composition | MoviePy, FFmpeg |
| Audio | MoviePy, FFmpeg |
| Data logging | CSV, pandas |
| Environment | Conda, Python 3.11 |

---

## Project Architecture

```text
marketing-video-generator/
│
├── app.py                    # Gradio UI
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
├── TROUBLESHOOTING.md         # Engineering notes and common problems
├── PROJECT_FLOW.md            # Pipeline flow explanation
│
├── input/                     # Optional local input images
├── output/                    # Generated outputs, plans, shots, logs
├── assets/
│   ├── music/                 # background.mp3
│   ├── sfx/                   # whoosh.mp3, shimmer.mp3
│   ├── fonts/
│   └── logos/
│
├── data/
│   └── runs.csv               # generation metadata and scoring
│
├── configs/
│   └── styles.json            # style templates
│
└── modules/
    ├── planner.py             # local Qwen scene planning
    ├── preprocess.py          # product image preprocessing
    ├── shot_builder.py        # scene image creation
    ├── composer.py            # final video composition
    ├── audio_system.py        # music/SFX handling
    ├── video_generator.py     # backend selection layer
    ├── prompt_builder.py      # future AI-video prompts
    ├── pipeline.py            # end-to-end generation pipeline
    ├── scorer.py              # scoring and CSV logging
    └── utils.py               # shared helpers
```

---

## How the Pipeline Works

```text
User input
   ↓
planner.py
   ↓
preprocess.py
   ↓
shot_builder.py
   ↓
video_generator.py
   ↓
composer.py + audio_system.py
   ↓
final MP4 / GIF
   ↓
scorer.py + runs.csv
```

### Full Pipeline Order

1. Get user input from Gradio.
2. Run local Qwen planner.
3. Generate structured JSON scene plan.
4. Preprocess product image.
5. Create base scenes using the template engine.
6. Prepare optional AI-video prompt jobs for future use.
7. Compose all scenes into a video.
8. Add captions/text, music, SFX, glow, particles, and transitions.
9. Export MP4 and optional GIF.
10. Save metadata to `data/runs.csv`.
11. Allow the user to score the result.

---

## Installation

### 1. Create Conda Environment

```cmd
conda create --prefix "D:\conda_envs\MarketingProject" python=3.11 -y
conda activate "D:\conda_envs\MarketingProject"
```

### 2. Install FFmpeg

```cmd
conda install -c conda-forge ffmpeg -y
ffmpeg -version
```

### 3. Install Python Packages

```cmd
pip install -r requirements.txt
```

If you do not have a requirements file yet, install the main packages manually:

```cmd
pip install gradio moviepy opencv-python pillow numpy pandas python-dotenv pydantic rembg onnxruntime ffmpeg-python
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
pip install transformers diffusers accelerate safetensors
```

---

## Running the App

```cmd
conda activate "D:\conda_envs\MarketingProject"
cd /d "D:\Projects\marketing-video-generator"
python app.py
```

Open the local Gradio URL shown in the terminal, usually:

```text
http://127.0.0.1:7860
```

---

## How to Use

1. Upload a clear product image.
2. Enter product name.
3. Enter product type.
4. Enter product description.
5. Select a style.
6. Select target audience.
7. Select duration.
8. Select output format: MP4 or GIF.
9. Click **Generate Video**.
10. Preview and download the output.
11. Score the result from 1 to 5.

---

## Example Input

```text
Product name: Luna Perfume
Product type: perfume
Product description: A luxury perfume with floral and woody notes made for confident women.
Style: luxury
Target audience: young professional women
Duration: 8 seconds
Output format: MP4
```

---

## Scoring System

Each output can be rated from 1 to 5 on:

- Product visibility
- Text readability
- Motion smoothness
- Style match
- Premium look
- Overall quality

The scores are saved in `data/runs.csv`. Later, this can be analyzed with pandas to identify which styles, prompts, and settings create the best outputs.

---

## Current MVP Scope

The current MVP focuses on reliability over perfection.

### Completed

- Working Gradio UI
- Local LLM planner
- Product image preprocessing
- Template-based shot builder
- Motion-based video composer
- Music and SFX system
- MP4/GIF export
- Scoring and metadata logging
- Future backend structure

### Not Yet Completed

- Full AI image-to-video generation
- True layer-based text animation
- Advanced product upscaling
- Advanced transitions
- Production deployment
- Cloud GPU support

---

## Future Improvements

1. Improve background quality.
2. Add better typography and text layout.
3. Add true text animation as separate layers.
4. Improve transitions and easing.
5. Add product enhancement/upscaling.
6. Add better color grading.
7. Improve motion smoothness.
8. Analyze scores using pandas/EDA.
9. Integrate ComfyUI for selected AI-generated scenes.
10. Deploy a lightweight public demo.

---

## Engineering Decisions

### Why template motion first?

Open AI video models are heavy, GPU-hungry, and inconsistent. A template-motion engine guarantees working output on a normal laptop while still producing clean ads.

### Why JSON scene plans?

JSON makes the planner output usable by the rest of the pipeline. The video generator can programmatically read scene type, duration, text, and motion.

### Why backend structure?

The project should not depend on one model or tool. The backend system allows switching between template motion, ComfyUI, and Diffusers later.

### Why add scoring?

The scoring system turns subjective video quality into data. Over time, scores can show which styles, prompts, and settings work best.

---

## Known Limitations

- AI planner can sometimes produce imperfect JSON, so fallback handling is included.
- Background removal quality depends heavily on the input image.
- GIF export has lower quality and larger file size than MP4.
- Full AI video generation is not enabled yet due to hardware limitations.
- Local generation can take time on laptops without a dedicated GPU.

---

## License and Asset Notes

Use royalty-free or properly licensed music and sound effects for demos or client work. Recommended sources include Pixabay Music, Mixkit, and YouTube Audio Library. Always check the license before using assets commercially.

---

## Author

Built as a practical AI + automation project to demonstrate local AI planning, image preprocessing, video composition, UI development, and data-driven improvement.
