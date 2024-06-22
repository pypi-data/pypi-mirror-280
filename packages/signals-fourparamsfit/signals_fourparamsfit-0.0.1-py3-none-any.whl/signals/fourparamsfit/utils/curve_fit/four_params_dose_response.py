import numpy as np
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score
from pydantic import BaseModel
from typing import List, Tuple, Optional
from dataclasses import dataclass
from abc import ABC, abstractmethod



@dataclass
class DataDoseResponse:
    """Data for the 4PL fit."""
    dose: List[float]
    response: List[float]
    response_err: Optional[List[float]] = None

@dataclass
class ParamsDoseResponseFourFit:
    """Fitted Parameters."""
    Lower: float
    Upper: float
    IC50: float
    Hill: float
    
    
@dataclass
class ErrParamsDoseResponseFourFit:
    """Errors of the fitted parameters."""
    Lower: float
    Upper: float
    IC50: float
    Hill: float
    
    
@dataclass
class MetricsDoseResponseFourFit:
    """Metrics of the fit."""
    R2: float
    Chi_square: float


@dataclass
class ResultFitFourParamsDoseResponse:
    "Fit results for the 4PL fit."
    Params:ParamsDoseResponseFourFit
    ErrParams: ErrParamsDoseResponseFourFit
    Metrics: MetricsDoseResponseFourFit
    


@dataclass
class ConfigInitialDoseResponseFourFitParams:
    """Initial parameters for the 4PL fit."""
    Lower: Optional[float] = None
    Upper: Optional[float]= None
    IC50: Optional[float]= None
    Hill: Optional[float]= None


@dataclass
class ConfigFixedDoseResponseFourFitParams:
    """Fixed parameters for the 4PL fit."""
    Lower: bool = False
    Upper: bool= False
    IC50: bool= False
    Hill: bool= False


@dataclass
class ConfigBoundsDoseResponseFourFit:
    """Bounds for the 4PL fit."""
    Lower: Optional[List[float]] 
    Upper: Optional[List[float]]
    IC50:Optional[List[float]] 
    Hill: Optional[List[float] ]


@dataclass
class ConfigFitDoseResponse:
    """Configuration for the 4PL fit."""
    InitialParams: ConfigInitialDoseResponseFourFitParams
    FixedParams: ConfigFixedDoseResponseFourFitParams
    Bounds: ConfigBoundsDoseResponseFourFit


def modify_bounds_for_fixed_params(config: ConfigFitDoseResponse) -> ConfigFitDoseResponse:
    """
    Modify the bounds of the fixed parameters.
    
    Parameters
    ----------
    fix_params : ConfigFixedDoseResponseFourFitParams
        Fixed parameters.
    initial_params : List[float]
    """
    if config.FixedParams.Lower:
        config.Bounds.Lower = [config.InitialParams.Lower, config.InitialParams.Lower * (1+1e-9)]
        
    if config.FixedParams.Upper:
        config.Bounds.Upper = [config.InitialParams.Upper, config.InitialParams.Upper * (1+1e-9)]
    
    if config.FixedParams.IC50:
        config.Bounds.IC50 = [config.InitialParams.IC50, config.InitialParams.IC50 * (1+1e-9)]
    
    if config.FixedParams.Hill:
        config.Bounds.Hill = [config.InitialParams.Hill, config.InitialParams.Hill * (1+1e-9)]

    return config
    

def modify_bounds_none_case(config_bounds = ConfigBoundsDoseResponseFourFit):
    if not config_bounds.Lower:
        config_bounds.Lower = [-np.inf, np.inf]
    if not config_bounds.Upper:
        config_bounds.Upper = [-np.inf, np.inf]
    if not config_bounds.IC50:
        config_bounds.IC50 = [-np.inf, np.inf]
    if not config_bounds.Hill:
        config_bounds.Hill = [-np.inf, np.inf]
    return config_bounds


@dataclass
class DoseResponseCurve(ABC):
    
    data: DataDoseResponse
    config: ConfigFitDoseResponse
    
    @abstractmethod
    def fit_curve(self) -> ResultFitFourParamsDoseResponse:
        pass


    
    

class DoseResponseFourParams(DoseResponseCurve):
    
    def fit_curve(self) -> ResultFitFourParamsDoseResponse:
        
        
        def fourparams(x, Lower, Upper, IC50, Hill):
            """
            four parameter logistic (4PL) curve.

            Parameters
            ----------
            x : array_like
                The dose values.
            Lower : float
                The minimum asymptote. In a bioassay where you have a standard curve, this can be thought of as the response value at 0 concentration.
            Upper : float
                The maximum asymptote. In a bioassay where you have a standard curve, this can be thought of as the response value for infinite concentration.
            IC50 : float
                The inflection point. In a bioassay where you have a standard curve, this is the concentration of analyte that gives a response halfway between Lower and Upper.
            Hill : float
                The Hill's slope. This describes the steepness of the family of curves.
            """
            return ((Lower - Upper) / (1.0 + (x / IC50) ** Hill)) + Upper
        
        
        
        config = modify_bounds_for_fixed_params(self.config)
        initial_params = [config.InitialParams.Lower, config.InitialParams.Upper, config.InitialParams.IC50, config.InitialParams.Hill]
        
        config.Bounds = modify_bounds_none_case(config_bounds = config.Bounds)
        lower_bounds = [config.Bounds.Lower[0], config.Bounds.Upper[0], config.Bounds.IC50[0], config.Bounds.Hill[0]]
        upper_bounds = [config.Bounds.Lower[1], config.Bounds.Upper[1], config.Bounds.IC50[1], config.Bounds.Hill[1]]
        params, covariance = curve_fit(
                                        fourparams, 
                                        self.data.dose, 
                                        self.data.response, 
                                        p0=initial_params, 
                                        sigma=self.data.response_err, 
                                        bounds=(lower_bounds, upper_bounds), 
                                        absolute_sigma=False)

        params_dose_response = ParamsDoseResponseFourFit(Lower=params[0], Upper=params[1], IC50=params[2], Hill=params[3])
        params_errors = np.sqrt(np.diag(covariance))
        errparamsfourfit =  ErrParamsDoseResponseFourFit(Lower=params_errors[0], Upper=params_errors[1], IC50=params_errors[2], Hill=params_errors[3])
        
        r_squared = r2_score(self.data.response, fourparams( self.data.dose, *params))
        
        chisq = None
        
        if self.data.response_err is not None:
            residual = self.data.response - fourparams( self.data.dose, *params)      
            chisq = np.sum((residual/self.data.response_err)**2)
        
        metrics = MetricsDoseResponseFourFit(R2=r_squared, Chi_square=chisq)  
        
        return ResultFitFourParamsDoseResponse(
                                        Params=params_dose_response, 
                                        ErrParams=errparamsfourfit, 
                                        Metrics=metrics)
        
        
