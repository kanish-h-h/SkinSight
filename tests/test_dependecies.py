#!/usr/bin/env python3
import sys
import pkg_resources

# Required packages and versions (match requirements.txt)
REQUIREMENTS = {
    "tensorflow": "2.10.0",
    "opencv-python-headless": "4.7.0.72",
    "huggingface-hub": "0.16.4"
}


def test_tensorflow_gpu():
    """Verify TensorFlow can detect GPU."""
    import tensorflow as tf
    gpu_available = tf.config.list_physical_devices('GPU')
    assert gpu_available, "GPU not detected by TensorFlow!"
    print(f"✅ TensorFlow {tf.__version__} sees GPU: {gpu_available}")


def test_package_versions():
    """Check all package versions."""
    failures = []
    for pkg, expected_version in REQUIREMENTS.items():
        try:
            installed_version = pkg_resources.get_distribution(pkg).version
            if installed_version != expected_version:
                failures.append(
                    f"{pkg} (expected: {expected_version}, got: {installed_version})")
        except pkg_resources.DistributionNotFound:
            failures.append(f"{pkg} not installed")

    if failures:
        print("❌ Version mismatches:")
        print("\n".join(failures))
        sys.exit(1)
    print("✅ All package versions match requirements.txt")


if __name__ == "__main__":
    print("Running dependency tests...")
    test_package_versions()
    test_tensorflow_gpu()
    print("All tests passed!")
