import psutil
import http.client
import json
import time


def main():
    while True:
        print("CPU: \n")
        getCPUUsage()

        print("\n\nMem: \n")
        getMemUsage()

        print("\n\nDisk: \n")
        getDiskUsage()

        print("\n\nNetwork: \n")
        getNetworkUsage()

        time.sleep(10 * 60)    # Sleep for 10 minutes


def getCPUUsage():
    print("CPU usage %:", psutil.cpu_percent(), "%")
    print("CPU count:", psutil.cpu_count(), "cores")

    cpuUsagePercent = psutil.cpu_percent(1)
    print("CPU usage in last 10 secs:", cpuUsagePercent, "%")


def getMemUsage():
    print("Mem Total:",
          int(psutil.virtual_memory().total / (1024 * 1024)), "MB")

    print("Mem Used:",
          int(psutil.virtual_memory().used / (1024 * 1024)), "MB")

    print("Mem Available:",
          int(psutil.virtual_memory().available / (1024 * 1024)), "MB")

    memUsagePercent = psutil.virtual_memory().percent

    print("Mem Usage %:", memUsagePercent, "%")
    print("Swap Usage %:", psutil.swap_memory().percent, "%")


def getDiskUsage():
    for dp in psutil.disk_partitions():
        print("\nDisk usage of partition", dp.mountpoint, ":")

        print("Total:",
              int(psutil.disk_usage(dp.mountpoint).total / (1024 * 1024)),
              "MB")

        print("Used:",
              int(psutil.disk_usage(dp.mountpoint).used / (1024 * 1024)),
              "MB")

        print("Free:",
              int(psutil.disk_usage(dp.mountpoint).free / (1024 * 1024)),
              "MB")

        diskUsagePercent = psutil.disk_usage(dp.mountpoint).percent
        print("Used %:", diskUsagePercent, "%")


def getNetworkUsage():
    print("Total bytes sent:",
          psutil.net_io_counters().bytes_sent,
          "Bytes")

    print("Total bytes received:",
          psutil.net_io_counters().bytes_recv,
          "Bytes")

    print("Total packets sent:",
          psutil.net_io_counters().packets_sent,
          "Packets")

    print("Total packets received:",
          psutil.net_io_counters().packets_recv,
          "Packets")

    print("Total incoming packets dropped:",
          psutil.net_io_counters().dropin,
          "Packets")

    print("Total outgoing packets dropped:",
          psutil.net_io_counters().dropout,
          "Packets")


if __name__ == "__main__":
    main()