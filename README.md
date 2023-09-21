# Real and Fake Project
## Master Thesis Thema: 
- Comparison of the Detection Sensitivities of Human and Full-Reference Image Quality Assessment Models to Distortions in Natural and Non-natural Images
### Measure JND by Psychopy
- We decide to use 2AFC (Two-Alternative Forced Choice)
QUEST procedure (a bayesian adaptive psychometric method)
Find the Just noticeable difference (JND)- minimum detectable distortion intensity
### Heeger-Bergen texture synthesis algorithm
- Retain the first-order statistics of both its pixel intensity and responses to multi-orientation and multi-scale filters

### Models
- Traditional: 
- MSE, NLPD : low-level features
- SSIM, MS SSIM: structure information
- DL-based:
- LPIPS: deep features extracted by VGG-16
- DISTS: the combination of deep features and structure information

