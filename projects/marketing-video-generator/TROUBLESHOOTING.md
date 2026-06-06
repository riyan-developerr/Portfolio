\# Troubleshooting and Engineering Notes



\## 1. Tool or model is not available



\### Problem

A model may be removed, gated, too slow, or not compatible with our system.



\### Solution

Do not hardcode the project around one specific model.



Our project uses a backend structure:



\- TemplateMotionGenerator

\- ComfyUIGenerator

\- DiffusersGenerator



If one backend fails, we can switch to another without rewriting the full app.



\### Current fallback

The default backend is:



```text

TemplateMotionGenerator

