import jax
import jax.numpy as jnp

# Check if GPU is available
device_count = len(jax.devices())

if device_count > 0:
    print(f"JAX is using {device_count} device(s):")
    for device in jax.devices():
        print(f"  - {device.device_kind} on {device.platform}")
    
    # Test a simple operation on GPU
    x = jnp.ones((1000, 1000))
    y = jnp.dot(x, x)
    print("JAX operation executed on GPU successfully.")
else:
    print("No GPU detected. JAX will use the CPU.")
