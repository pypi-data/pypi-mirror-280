import matplotlib.pyplot as plt


class MonitoringAnalysis:
    """
    A class to record and plot data for performance monitoring.
    """
    def __init__(self):
        self.data = []

    def record_data(self, value):
        self.data.append(value)

    def plot_data(self):
        plt.plot(self.data)
        plt.xlabel('Request (nth)')
        plt.ylabel('Response Time (s)')
        plt.title('Performance Monitoring')
        plt.show()
