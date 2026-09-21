"""
Forge Neo DOM selector map for critical components.

Provides explicit CSS selectors as fallback for components that cannot be
resolved through either blocks.ui_loadsave.component_mapping or ui-config.json.

Used when both Gradio component ID and ui-config DOM query mechanisms fail.
"""

FORGE_NEO_SELECTORS = {
    # txt2img generation settings
    "txt2img/Sampling steps/value":       "#txt2img_steps input",
    "txt2img/CFG Scale/value":            "#txt2img_cfg_scale input",
    "txt2img/Sampling method/value":      "#txt2img_sampling input",
    "txt2img/Schedule type/value":        "#txt2img_scheduler input",
    "txt2img/Width/value":                "#txt2img_width input",
    "txt2img/Height/value":               "#txt2img_height input",
    "txt2img/Distilled CFG Scale/value":  "#txt2img_distilled_cfg_scale input",

    # img2img generation settings
    "img2img/Denoising strength/value":   "#img2img_denoising_strength input",
    "img2img/Sampling steps/value":       "#img2img_steps input",
    "img2img/CFG Scale/value":            "#img2img_cfg_scale input",
    "img2img/Sampling method/value":      "#img2img_sampling input",
    "img2img/Schedule type/value":        "#img2img_scheduler input",
    "img2img/Width/value":                "#img2img_width input",
    "img2img/Height/value":               "#img2img_height input",
    "img2img/Distilled CFG Scale/value":  "#img2img_distilled_cfg_scale input",

    # Forge Neo model selection controls. The underlying values are also
    # exposed through shared.opts, but these selectors keep the visible UI in
    # sync when a saved config is restored.
    "forge_preset/value":                 "#forge_ui_preset input",
    "forge_unet_storage_dtype/value":     "#forge_ui_dtype input",
}
