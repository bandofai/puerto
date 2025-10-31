#!/usr/bin/env python3
"""
Time Series Forecasting Template

A comprehensive framework for time series forecasting with multiple models,
stationarity testing, and forecast evaluation.

Author: Data Scientist Plugin
Version: 1.0.0
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from statsmodels.tsa.stattools import adfuller, kpss, acf, pacf
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.arima.model import ARIMA
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from sklearn.metrics import mean_squared_error, mean_absolute_error, mean_absolute_percentage_error
import warnings
warnings.filterwarnings('ignore')

# Set style
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)


class TimeSeriesForecaster:
    """
    Time Series Forecasting Framework

    Supports:
    - Stationarity testing
    - Seasonal decomposition
    - Multiple forecasting models (ARIMA, Seasonal Naive, Moving Average)
    - Model comparison and selection
    - Forecast evaluation
    """

    def __init__(self, data, date_col=None, value_col=None, freq='D'):
        """
        Initialize forecaster

        Args:
            data: DataFrame with time series data OR Series with datetime index
            date_col: Column name for dates (if DataFrame)
            value_col: Column name for values (if DataFrame)
            freq: Frequency of time series ('D'=daily, 'M'=monthly, etc.)
        """
        if isinstance(data, pd.DataFrame):
            if date_col is None or value_col is None:
                raise ValueError("Must specify date_col and value_col for DataFrame")

            self.ts = data.set_index(date_col)[value_col].copy()
        else:
            self.ts = data.copy()

        # Ensure datetime index
        self.ts.index = pd.to_datetime(self.ts.index)
        self.ts = self.ts.asfreq(freq)

        self.freq = freq
        self.models = {}
        self.forecasts = {}

    def explore(self):
        """
        Exploratory analysis of time series

        Includes:
        - Summary statistics
        - Visualization
        - Stationarity tests
        - Seasonal decomposition
        """
        print("=" * 70)
        print("TIME SERIES EXPLORATION")
        print("=" * 70)

        # Summary statistics
        print(f"\nSummary Statistics:")
        print(f"  Start date: {self.ts.index.min()}")
        print(f"  End date: {self.ts.index.max()}")
        print(f"  Periods: {len(self.ts)}")
        print(f"  Frequency: {self.freq}")
        print(f"  Mean: {self.ts.mean():.2f}")
        print(f"  Std Dev: {self.ts.std():.2f}")
        print(f"  Min: {self.ts.min():.2f}")
        print(f"  Max: {self.ts.max():.2f}")

        # Missing values
        missing = self.ts.isnull().sum()
        if missing > 0:
            print(f"\n⚠ Warning: {missing} missing values ({missing/len(self.ts):.1%})")

        # Visualize time series
        self._plot_timeseries()

        # Test stationarity
        self._test_stationarity()

        # Decompose (if enough data)
        if len(self.ts) >= 24:  # Need at least 2 full cycles
            self._decompose()

        # ACF and PACF
        self._plot_acf_pacf()

    def _plot_timeseries(self):
        """Plot time series"""
        fig, axes = plt.subplots(2, 1, figsize=(12, 8))

        # Line plot
        axes[0].plot(self.ts.index, self.ts.values, linewidth=1.5)
        axes[0].set_xlabel('Date')
        axes[0].set_ylabel('Value')
        axes[0].set_title('Time Series Plot')
        axes[0].grid(True, alpha=0.3)

        # Distribution
        axes[1].hist(self.ts.values, bins=30, edgecolor='black', alpha=0.7)
        axes[1].set_xlabel('Value')
        axes[1].set_ylabel('Frequency')
        axes[1].set_title('Distribution')
        axes[1].grid(True, alpha=0.3)

        plt.tight_layout()
        plt.savefig('timeseries_exploration.png', dpi=300, bbox_inches='tight')
        print("\n✓ Visualization saved: timeseries_exploration.png")
        plt.close()

    def _test_stationarity(self):
        """
        Test if time series is stationary

        Uses both ADF and KPSS tests
        """
        print("\n" + "=" * 70)
        print("STATIONARITY TESTS")
        print("=" * 70)

        # ADF test (H0: non-stationary)
        adf_result = adfuller(self.ts.dropna(), autolag='AIC')

        print("\nAugmented Dickey-Fuller Test:")
        print(f"  ADF Statistic: {adf_result[0]:.4f}")
        print(f"  p-value: {adf_result[1]:.4f}")
        print(f"  Critical values:")
        for key, value in adf_result[4].items():
            print(f"    {key}: {value:.4f}")

        if adf_result[1] < 0.05:
            print(f"  ✓ Result: STATIONARY (reject H0 at 5% level)")
            adf_stationary = True
        else:
            print(f"  ✗ Result: NON-STATIONARY (fail to reject H0)")
            adf_stationary = False

        # KPSS test (H0: stationary)
        kpss_result = kpss(self.ts.dropna(), regression='c', nlags='auto')

        print("\nKwiatkowski-Phillips-Schmidt-Shin Test:")
        print(f"  KPSS Statistic: {kpss_result[0]:.4f}")
        print(f"  p-value: {kpss_result[1]:.4f}")
        print(f"  Critical values:")
        for key, value in kpss_result[3].items():
            print(f"    {key}: {value:.4f}")

        if kpss_result[1] > 0.05:
            print(f"  ✓ Result: STATIONARY (fail to reject H0 at 5% level)")
            kpss_stationary = True
        else:
            print(f"  ✗ Result: NON-STATIONARY (reject H0)")
            kpss_stationary = False

        # Combined interpretation
        print("\nCombined Interpretation:")
        if adf_stationary and kpss_stationary:
            print("  ✓ Series appears STATIONARY (both tests agree)")
            print("  → No differencing needed for ARIMA (d=0)")
        elif not adf_stationary and not kpss_stationary:
            print("  ✗ Series appears NON-STATIONARY (both tests agree)")
            print("  → Differencing recommended for ARIMA (d=1 or d=2)")
        else:
            print("  ? Tests disagree - series may be trend-stationary")
            print("  → Try differencing once and retest")

    def _decompose(self):
        """Seasonal decomposition"""
        print("\n" + "=" * 70)
        print("SEASONAL DECOMPOSITION")
        print("=" * 70)

        # Determine period based on frequency
        period_map = {
            'D': 7,      # Daily: weekly seasonality
            'W': 52,     # Weekly: yearly seasonality
            'M': 12,     # Monthly: yearly seasonality
            'Q': 4,      # Quarterly: yearly seasonality
        }

        period = period_map.get(self.freq, 12)

        if len(self.ts) < 2 * period:
            print(f"\n⚠ Not enough data for decomposition (need at least {2*period} periods)")
            return

        try:
            # Additive decomposition
            decomposition = seasonal_decompose(self.ts.dropna(), model='additive', period=period)

            # Plot
            fig, axes = plt.subplots(4, 1, figsize=(12, 10))

            # Original
            axes[0].plot(self.ts.index, self.ts.values)
            axes[0].set_ylabel('Original')
            axes[0].set_title('Seasonal Decomposition')
            axes[0].grid(True, alpha=0.3)

            # Trend
            axes[1].plot(decomposition.trend.index, decomposition.trend.values)
            axes[1].set_ylabel('Trend')
            axes[1].grid(True, alpha=0.3)

            # Seasonal
            axes[2].plot(decomposition.seasonal.index, decomposition.seasonal.values)
            axes[2].set_ylabel('Seasonal')
            axes[2].grid(True, alpha=0.3)

            # Residual
            axes[3].plot(decomposition.resid.index, decomposition.resid.values)
            axes[3].set_ylabel('Residual')
            axes[3].set_xlabel('Date')
            axes[3].grid(True, alpha=0.3)

            plt.tight_layout()
            plt.savefig('seasonal_decomposition.png', dpi=300, bbox_inches='tight')
            print("\n✓ Decomposition saved: seasonal_decomposition.png")
            plt.close()

            # Strength of seasonality
            seasonal_strength = 1 - (decomposition.resid.var() / (decomposition.resid + decomposition.seasonal).var())
            trend_strength = 1 - (decomposition.resid.var() / (decomposition.resid + decomposition.trend).var())

            print(f"\nDecomposition Metrics:")
            print(f"  Seasonal strength: {seasonal_strength:.4f}")
            print(f"  Trend strength: {trend_strength:.4f}")

        except Exception as e:
            print(f"\n⚠ Decomposition failed: {e}")

    def _plot_acf_pacf(self):
        """Plot ACF and PACF"""
        fig, axes = plt.subplots(1, 2, figsize=(14, 4))

        # ACF
        plot_acf(self.ts.dropna(), lags=min(40, len(self.ts)//2), ax=axes[0])
        axes[0].set_title('Autocorrelation Function (ACF)')

        # PACF
        plot_pacf(self.ts.dropna(), lags=min(40, len(self.ts)//2), ax=axes[1])
        axes[1].set_title('Partial Autocorrelation Function (PACF)')

        plt.tight_layout()
        plt.savefig('acf_pacf.png', dpi=300, bbox_inches='tight')
        print("\n✓ ACF/PACF saved: acf_pacf.png")
        plt.close()

    def fit_arima(self, order=(1, 1, 1), train_size=0.8):
        """
        Fit ARIMA model

        Args:
            order: (p, d, q) order for ARIMA
                   p: AR order (use PACF to determine)
                   d: Differencing order (0 if stationary, 1 or 2 if not)
                   q: MA order (use ACF to determine)
            train_size: Proportion of data for training

        Returns:
            Fitted ARIMA model
        """
        print("\n" + "=" * 70)
        print(f"FITTING ARIMA{order}")
        print("=" * 70)

        # Split data
        split_idx = int(len(self.ts) * train_size)
        train = self.ts[:split_idx]
        test = self.ts[split_idx:]

        print(f"\nTrain size: {len(train)} ({train_size:.0%})")
        print(f"Test size: {len(test)} ({1-train_size:.0%})")

        # Fit model
        model = ARIMA(train, order=order)
        fitted_model = model.fit()

        print("\n" + fitted_model.summary().as_text())

        # Store model
        self.models['arima'] = {
            'model': fitted_model,
            'order': order,
            'train': train,
            'test': test
        }

        # Diagnostic plots
        fitted_model.plot_diagnostics(figsize=(12, 8))
        plt.tight_layout()
        plt.savefig('arima_diagnostics.png', dpi=300, bbox_inches='tight')
        print("\n✓ Diagnostics saved: arima_diagnostics.png")
        plt.close()

        return fitted_model

    def fit_naive_models(self, train_size=0.8):
        """
        Fit naive baseline models

        Models:
        - Naive: Last observation
        - Seasonal Naive: Same period last cycle
        - Mean: Historical mean
        - Drift: Linear trend from first to last
        """
        print("\n" + "=" * 70)
        print("FITTING BASELINE MODELS")
        print("=" * 70)

        # Split data
        split_idx = int(len(self.ts) * train_size)
        train = self.ts[:split_idx]
        test = self.ts[split_idx:]

        # Naive forecast (last value)
        naive_forecast = pd.Series([train.iloc[-1]] * len(test), index=test.index)

        # Mean forecast
        mean_forecast = pd.Series([train.mean()] * len(test), index=test.index)

        # Drift forecast (linear trend)
        slope = (train.iloc[-1] - train.iloc[0]) / (len(train) - 1)
        drift_forecast = pd.Series(
            [train.iloc[-1] + slope * (i + 1) for i in range(len(test))],
            index=test.index
        )

        # Store models
        self.models['naive'] = {'train': train, 'test': test, 'forecast': naive_forecast}
        self.models['mean'] = {'train': train, 'test': test, 'forecast': mean_forecast}
        self.models['drift'] = {'train': train, 'test': test, 'forecast': drift_forecast}

        print("\n✓ Baseline models fitted")

    def forecast(self, steps=None, model_name='arima'):
        """
        Generate forecast

        Args:
            steps: Number of steps to forecast (if None, uses test set length)
            model_name: Name of model to use

        Returns:
            Forecast series
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not fitted. Available: {list(self.models.keys())}")

        model_info = self.models[model_name]

        if model_name == 'arima':
            # ARIMA forecast
            fitted_model = model_info['model']
            if steps is None:
                steps = len(model_info['test'])

            forecast = fitted_model.forecast(steps=steps)

        else:
            # Baseline models already have forecasts
            forecast = model_info['forecast']

        self.forecasts[model_name] = forecast

        return forecast

    def evaluate(self, model_names=None):
        """
        Evaluate forecast accuracy

        Args:
            model_names: List of model names to evaluate (if None, evaluates all)

        Returns:
            DataFrame with metrics
        """
        if model_names is None:
            model_names = list(self.models.keys())

        print("\n" + "=" * 70)
        print("FORECAST EVALUATION")
        print("=" * 70)

        results = []

        for name in model_names:
            if name not in self.models:
                continue

            model_info = self.models[name]
            test = model_info['test']

            # Get forecast
            if name not in self.forecasts:
                self.forecast(model_name=name)

            forecast = self.forecasts[name]

            # Calculate metrics
            rmse = np.sqrt(mean_squared_error(test, forecast))
            mae = mean_absolute_error(test, forecast)
            mape = mean_absolute_percentage_error(test, forecast) * 100

            # Mean Error (bias)
            me = (forecast - test).mean()

            results.append({
                'Model': name,
                'RMSE': rmse,
                'MAE': mae,
                'MAPE': mape,
                'ME': me
            })

        results_df = pd.DataFrame(results)

        print("\n" + results_df.to_string(index=False))

        # Best model by RMSE
        best_idx = results_df['RMSE'].idxmin()
        best_model = results_df.loc[best_idx, 'Model']

        print(f"\n✓ Best model (by RMSE): {best_model}")

        return results_df

    def plot_forecast(self, model_name='arima', include_train=True):
        """
        Plot forecast vs actual

        Args:
            model_name: Model to plot
            include_train: Whether to include training data in plot
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not fitted")

        model_info = self.models[model_name]
        train = model_info['train']
        test = model_info['test']

        if model_name not in self.forecasts:
            self.forecast(model_name=model_name)

        forecast = self.forecasts[model_name]

        # Plot
        plt.figure(figsize=(14, 6))

        if include_train:
            plt.plot(train.index, train.values, label='Training Data', linewidth=1.5)

        plt.plot(test.index, test.values, label='Actual', color='green', linewidth=2)
        plt.plot(forecast.index, forecast.values, label='Forecast',
                color='red', linestyle='--', linewidth=2)

        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.title(f'Forecast: {model_name.upper()}')
        plt.legend()
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.savefig(f'forecast_{model_name}.png', dpi=300, bbox_inches='tight')
        print(f"\n✓ Forecast plot saved: forecast_{model_name}.png")
        plt.close()

    def plot_residuals(self, model_name='arima'):
        """
        Plot residual diagnostics

        Args:
            model_name: Model to analyze
        """
        if model_name not in self.models:
            raise ValueError(f"Model '{model_name}' not fitted")

        model_info = self.models[model_name]
        test = model_info['test']

        if model_name not in self.forecasts:
            self.forecast(model_name=model_name)

        forecast = self.forecasts[model_name]
        residuals = test - forecast

        # Plot
        fig, axes = plt.subplots(2, 2, figsize=(12, 10))

        # Residuals over time
        axes[0, 0].plot(residuals.index, residuals.values)
        axes[0, 0].axhline(y=0, color='r', linestyle='--')
        axes[0, 0].set_xlabel('Date')
        axes[0, 0].set_ylabel('Residuals')
        axes[0, 0].set_title('Residuals Over Time')
        axes[0, 0].grid(True, alpha=0.3)

        # Histogram
        axes[0, 1].hist(residuals.values, bins=20, edgecolor='black', alpha=0.7)
        axes[0, 1].set_xlabel('Residuals')
        axes[0, 1].set_ylabel('Frequency')
        axes[0, 1].set_title('Residual Distribution')
        axes[0, 1].grid(True, alpha=0.3)

        # Q-Q plot
        stats.probplot(residuals.values, dist="norm", plot=axes[1, 0])
        axes[1, 0].set_title('Q-Q Plot')

        # ACF of residuals
        from statsmodels.graphics.tsaplots import plot_acf
        plot_acf(residuals.dropna(), lags=min(20, len(residuals)//2), ax=axes[1, 1])
        axes[1, 1].set_title('ACF of Residuals')

        plt.tight_layout()
        plt.savefig(f'residuals_{model_name}.png', dpi=300, bbox_inches='tight')
        print(f"\n✓ Residual analysis saved: residuals_{model_name}.png")
        plt.close()


# ==============================================================================
# EXAMPLE USAGE
# ==============================================================================

if __name__ == "__main__":
    print("\n" + "=" * 70)
    print("TIME SERIES FORECASTING - EXAMPLE")
    print("=" * 70)

    # Generate sample time series data (with trend and seasonality)
    np.random.seed(42)
    n = 365  # One year of daily data

    dates = pd.date_range(start='2023-01-01', periods=n, freq='D')

    # Trend + Seasonality + Noise
    trend = np.linspace(100, 150, n)
    seasonal = 10 * np.sin(2 * np.pi * np.arange(n) / 7)  # Weekly seasonality
    noise = np.random.normal(0, 5, n)

    values = trend + seasonal + noise

    ts_data = pd.Series(values, index=dates)

    # Initialize forecaster
    forecaster = TimeSeriesForecaster(ts_data, freq='D')

    # Explore data
    forecaster.explore()

    # Fit ARIMA
    forecaster.fit_arima(order=(1, 1, 1), train_size=0.8)

    # Fit baseline models
    forecaster.fit_naive_models(train_size=0.8)

    # Evaluate all models
    results = forecaster.evaluate()

    # Plot best model forecast
    best_model = results.loc[results['RMSE'].idxmin(), 'Model']
    forecaster.plot_forecast(model_name=best_model)

    # Residual analysis
    forecaster.plot_residuals(model_name=best_model)

    print("\n\n" + "=" * 70)
    print("FORECASTING COMPLETE")
    print("=" * 70)
    print("\nGenerated files:")
    print("  - timeseries_exploration.png")
    print("  - seasonal_decomposition.png")
    print("  - acf_pacf.png")
    print("  - arima_diagnostics.png")
    print(f"  - forecast_{best_model}.png")
    print(f"  - residuals_{best_model}.png")
