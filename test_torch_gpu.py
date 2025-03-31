import torch

def test_pytorch_gpu():
    print("PyTorch version:", torch.__version__)
    gpu_available = torch.cuda.is_available()
    print("CUDA available:", gpu_available)
    
    if gpu_available:
        device = torch.device("cuda")
        print("Using device:", torch.cuda.get_device_name(0))
        
        # Create a random tensor and move it to the GPU
        x = torch.rand(3, 3).to(device)
        print("Tensor on GPU:", x)
    else:
        print("CUDA is not available. Running on CPU.")
        
if __name__ == "__main__":
    test_pytorch_gpu()