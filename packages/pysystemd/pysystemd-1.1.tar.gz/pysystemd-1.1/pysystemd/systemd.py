import subprocess
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ServiceStatus:
    """Check the status of a service on your system."""
    def __init__(self, service):
        self.service = service

    def is_running(self):
        """Check if the service is running. Returns True if running, False otherwise."""
        try:
            output = subprocess.check_output(f"systemctl is-active {self.service}", shell=True)
            return output.strip() == b'active'
        except subprocess.CalledProcessError:
            return False

    def is_enabled(self):
        """Check if the service is enabled. Returns True if enabled, False otherwise."""
        try:
            output = subprocess.check_output(f"systemctl is-enabled {self.service}", shell=True)
            return output.strip() == b'enabled'
        except subprocess.CalledProcessError:
            return False

    def get_status(self):
        """Get detailed status of the service."""
        try:
            output = subprocess.check_output(f"systemctl status {self.service}", shell=True)
            return output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            logging.error(f"Error getting status for service {self.service}: {e}")
            return None

class ServiceManager:
    """Manage services: start, stop, restart, reload, enable, and disable."""
    def __init__(self, service):
        self.service = service

    def start(self):
        """Start a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl start {self.service}", shell=True)
            return ServiceStatus(self.service).is_running()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error starting service {self.service}: {e}")
            return False

    def stop(self):
        """Stop a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl stop {self.service}", shell=True)
            return not ServiceStatus(self.service).is_running()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error stopping service {self.service}: {e}")
            return False

    def restart(self):
        """Restart a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl restart {self.service}", shell=True)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Error restarting service {self.service}: {e}")
            return False

    def reload(self):
        """Reload a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl reload {self.service}", shell=True)
            return True
        except subprocess.CalledProcessError as e:
            logging.error(f"Error reloading service {self.service}: {e}")
            return False

    def enable(self):
        """Enable a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl enable {self.service}", shell=True)
            return ServiceStatus(self.service).is_enabled()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error enabling service {self.service}: {e}")
            return False

    def disable(self):
        """Disable a service. Returns True if succeeded."""
        try:
            subprocess.check_output(f"systemctl disable {self.service}", shell=True)
            return not ServiceStatus(self.service).is_enabled()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error disabling service {self.service}: {e}")
            return False

class ServiceLister:
    """List various service statuses."""
    @staticmethod
    def list_all():
        """List all services."""
        services = []
        try:
            services = [f for f in os.listdir("/etc/systemd/system") + os.listdir("/lib/systemd/system") if f.endswith(".service")]
        except Exception as e:
            logging.error(f"Error listing services: {e}")
        return services

    @staticmethod
    def list_running():
        """List all running services."""
        running_services = []
        for service in ServiceLister.list_all():
            if ServiceStatus(service).is_running():
                running_services.append(service)
        return running_services

    @staticmethod
    def list_not_running():
        """List all not running services."""
        not_running_services = []
        for service in ServiceLister.list_all():
            if not ServiceStatus(service).is_running():
                not_running_services.append(service)
        return not_running_services

    @staticmethod
    def list_enabled():
        """List all enabled services."""
        enabled_services = []
        for service in ServiceLister.list_all():
            if ServiceStatus(service).is_enabled():
                enabled_services.append(service)
        return enabled_services

    @staticmethod
    def list_disabled():
        """List all disabled services."""
        disabled_services = []
        for service in ServiceLister.list_all():
            if not ServiceStatus(service).is_enabled():
                disabled_services.append(service)
        return disabled_services

class PowerManager:
    """Manage power operations: poweroff, reboot, rescue, and suspend."""
    @staticmethod
    def poweroff():
        """Power off the system."""
        try:
            subprocess.check_output("systemctl poweroff", shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error powering off: {e}")

    @staticmethod
    def reboot():
        """Reboot the system."""
        try:
            subprocess.check_output("systemctl reboot", shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error rebooting: {e}")

    @staticmethod
    def rescue():
        """Boot to rescue mode."""
        try:
            subprocess.check_output("systemctl rescue", shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error entering rescue mode: {e}")

    @staticmethod
    def suspend():
        """Suspend the system."""
        try:
            subprocess.check_output("systemctl suspend", shell=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error suspending: {e}")

class SystemStatus:
    """Get system status information."""
    @staticmethod
    def uptime():
        """Get the system uptime."""
        try:
            output = subprocess.check_output("uptime -p", shell=True)
            return output.decode('utf-8').strip()
        except subprocess.CalledProcessError as e:
            logging.error(f"Error getting system uptime: {e}")
            return None

    @staticmethod
    def load_average():
        """Get the system load average."""
        try:
            output = subprocess.check_output("uptime", shell=True)
            load_avg = output.decode('utf-8').split()[-3:]
            return " ".join(load_avg)
        except subprocess.CalledProcessError as e:
            logging.error(f"Error getting system load average: {e}")
            return None