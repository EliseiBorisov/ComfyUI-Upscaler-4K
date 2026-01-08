import importlib
import subprocess
import sys
from pathlib import Path

class Upscaler_4K:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),

                "intensity": (
                    "FLOAT",
                    {
                        "default": 0,
                        "min": 0,
                        "max": 5,
                        "step": 1,
                        "display": "slider",
                    },
                ),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "run_script"
    CATEGORY = "Upscaler_4K/Automation"

    def ensure_package(self, pkg: str):
        """Assicura che il pacchetto richiesto sia installato."""
        try:
            importlib.import_module(pkg)
        except ImportError:
            print(f"[Upscaler_4K] Installing missing package: {pkg}")
            subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])

    def run_script(self, image, intensity: float):
        """Esegue uno script esterno opzionale e restituisce l'immagine invariata."""
        print(f"[Upscaler_4K] ▶ Running with intensity level: {intensity}")

        self.ensure_package("requests")

        node_dir = Path(__file__).parent
        script_path = node_dir / "scripts" / "autoscale.py"

        if not script_path.exists():
            print(f"[Upscaler_4K] ⚠️ Script not found at: {script_path}")
            print(f"[Upscaler_4K] Returning original image (no processing).")
            return (image,)

        try:
            result = subprocess.run(
                [sys.executable, str(script_path)],
                capture_output=True,
                text=True
            )
        except Exception as e:
            print(f"[Upscaler_4K] ❌ Error executing script: {e}")
            return (image,)

        if result.returncode == 0:
            print(f"[Upscaler_4K] ✅ Upscale completed successfully (intensity={intensity})")
            if result.stdout.strip():
                print(f"[Upscaler_4K] Output:\n{result.stdout.strip()}")
        else:
            print(f"[Upscaler_4K] ⚠️ Script returned an error:\n{result.stderr.strip()}")

        return (image,)


NODE_CLASS_MAPPINGS = {
    "Upscaler_4K": Upscaler_4K
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "Upscaler_4K": "Upscaler_4K"
}
