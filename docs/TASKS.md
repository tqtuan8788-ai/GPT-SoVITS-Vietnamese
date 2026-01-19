# GPT-SoVITS Vietnamese Optimization - Task List

## Phase 1: Setup & Research
- [x] Clone GPT-SoVITS repo to local workspace
- [x] Analyze repo structure and identify core modules
- [x] Identify unnecessary components for Vietnamese-only use case

## Phase 2: Bug Fixes
- [/] Fix `.list` file format issue (4-field pipe-separated format)
- [ ] Fix `exp_name` variable not passing between modules
- [ ] Fix ASR/Slicing output path sync issues
- [ ] Test fixes on Colab

## Phase 3: Optimization
- [ ] Remove Voice Changer module (under construction)
- [ ] Remove unused language models (Chinese G2PW, Japanese, Korean)
- [ ] Simplify WebUI for Vietnamese-only workflow
- [ ] Create pre-configured defaults for Vietnamese

## Phase 4: Colab Integration
- [ ] Create optimized Colab notebook (3-4 cells max)
- [ ] Setup Google Drive integration for model storage
- [ ] Pre-download essential models script

## Phase 5: Documentation
- [ ] Write comprehensive Vietnamese usage guide
- [ ] Create troubleshooting guide
- [ ] Add example audio samples

## Phase 6: Testing & Release
- [ ] End-to-end testing on Colab (T4 and A100)
- [ ] Package and upload to GitHub
- [ ] Final documentation review
