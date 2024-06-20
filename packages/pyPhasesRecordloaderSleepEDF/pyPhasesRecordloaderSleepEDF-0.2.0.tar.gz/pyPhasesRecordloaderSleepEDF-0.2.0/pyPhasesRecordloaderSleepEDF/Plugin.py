from pyPhases import PluginAdapter
from pyPhasesRecordloader import RecordLoader


class Plugin(PluginAdapter):
    def initPlugin(self):
        RecordLoader.registerRecordLoader(
            "RecordLoaderSleepEDF", "pyPhasesRecordloaderSleepEDF.recordLoaders"
        )
        path = self.getConfig("sleepedf-path")
        self.project.setConfig("loader.sleepedf.filePath", f"{path}")
