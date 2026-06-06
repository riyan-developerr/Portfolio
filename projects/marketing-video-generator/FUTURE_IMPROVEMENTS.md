# Future Improvements

This file records features intentionally skipped during the MVP build. The goal is to keep the current version stable and improve the project step by step.

## 1. Full AI Image-to-Video Generation

Potential approaches:

- ComfyUI workflow
- Diffusers-based Python workflow
- Cloud GPU / Colab / Kaggle

Reason skipped for MVP:

- Heavy models
- No dedicated GPU
- 8 GB RAM limitation
- Higher risk of instability

## 2. True Layer-Based Text Animation

Current version bakes text into scene images. Future version should separate:

- background layer
- product layer
- text layer
- glow/particles layer

This will allow real fade-in, slide-in, and animated typography.

## 3. Advanced Product Enhancement

Future upgrades:

- Real-ESRGAN or lightweight upscaling
- Better sharpening
- Edge cleanup after background removal
- Shadow/reflection refinement

## 4. Better Backgrounds

Improve style templates with:

- radial spotlights
- premium gradients
- subtle textures
- animated background elements
- style-specific layouts

## 5. Better Transitions

Future transition improvements:

- directional wipes
- masked light sweep transitions
- blur transitions
- smoother easing curves
- beat-synced cuts

## 6. Better Motion System

Future improvements:

- smoother parallax
- scene-specific motion presets
- product-safe camera movement
- better interpolation
- zoom/pan presets from style templates

## 7. API-Based LLM Option

Add optional cloud LLM support for:

- better scene plans
- stronger marketing copy
- better prompt generation

Local Qwen should remain as fallback.

## 8. Scoring Analysis Dashboard

Use pandas to analyze:

- best-performing styles
- common failure points
- average score by product type
- correlation between duration/style/backend and quality

## 9. Deployment

Potential deployment paths:

- temporary Gradio share link
- Hugging Face Spaces lightweight demo
- cloud VM
- portfolio website with demo video and GitHub link

## 10. Production Polish

Future production-level improvements:

- better error handling
- progress bar
- cancel generation button
- cache management
- asset/license management
- UI cleanup
- sample demo gallery
