import SimpleITK as sitk

class processor:
    def __init__(self):
        pass

    def read_nii(self, nii_path):
        img = sitk.ReadImage(nii_path)
        self.image = img
    
    def write_nii(self, output_path):
        if not hasattr(self, "image"):
            raise AttributeError("No image to write")
        sitk.WriteImage(self.image, output_path)
        print(f"Save image to {output_path}")

    def blur(self,sigma):
        gaussian = sitk.SmoothingRecursiveGaussianImageFilter()
        gaussian.SetSigma(sigma)
        self.img = gaussian.Execute(self.image)

    def resample(self, size=None,spacing=None,origin=None,direction=None,method=None):
        size = size or self.image.GetSize()
        spacing = spacing or self.image.GetSpacing()
        origin = origin or self.image.GetOrigin()
        direction = direction or self.image.GetDirection()
        method = method or "linear"
         
        resampler = sitk.ResampleImageFilter()
        resampler.SetReferenceImage(self.image)
        resampler.SetSize(size)
        resampler.SetOutputSpacing(spacing)
        resampler.SetOutputOrigin(origin)
        resampler.SetOutputDirection(direction)
        resampler.SetTransform(sitk.Transform())
        if method == "linear":
            resampler.SetInterpolator(sitk.sitkLinear)
        elif method == "nearest":
            resampler.SetInterpolator(sitk.sitkNearestNeighbor)
        
        self.image = resampler.Execute(self.image)
       
    
    def rescale(self, new_min=0, new_max=1):
        self.image = sitk.RescaleIntensity(self.image, new_min, new_max)

    
    def threshold(self, type="otsu", lower=0, upper=1):
        if type == "otsu":
            self.image = sitk.OtsuThreshold(self.image, lower, upper)
        elif type == "triangle":
            self.image = sitk.TriangleThreshold(self.image, lower, upper)
        elif type == "mean":
            self.image = sitk.MeanThreshold(self.image, lower, upper)
        elif type == "maximum":
            self.image = sitk.MaximumEntropyThreshold(self.image, lower, upper)
        
    
    
    def denoise(self, numIterations=5, conductanceScaling=1.0):
        self.image = sitk.CurvatureFlow(self.image, numIterations=numIterations, conductanceScaling=conductanceScaling)
        
    def edge_detection(self, lower=0, upper=1):
        self.image = sitk.CannyEdgeDetection(self.image, lower, upper)
    
