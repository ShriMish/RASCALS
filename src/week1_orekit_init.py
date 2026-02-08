import jpype
import jpype.imports
import os

# JVM DLL (Zulu JDK)
JVM_DLL = r"C:\Program Files\Zulu\zulu-25\bin\server\jvm.dll"

# Orekit JAR directory (NOT a single jar)
OREKIT_JAR_DIR = (
    r"C:\Users\Admin\Documents\spacecraft_digital_twin"
    r"\.venv\Lib\site-packages\orekit_jpype\jars\*"
)

assert os.path.exists(JVM_DLL), "JVM DLL not found"
assert os.path.exists(OREKIT_JAR_DIR[:-1]), "Orekit JAR directory not found"

if not jpype.isJVMStarted():
    jpype.startJVM(
        JVM_DLL,
        f"-Djava.class.path={OREKIT_JAR_DIR}",
        "--enable-native-access=ALL-UNNAMED",
        convertStrings=True
    )

print("JVM started with Orekit JARs on classpath")

# These imports MUST now work
from org.orekit.time import AbsoluteDate
from org.orekit.frames import FramesFactory

print("Orekit Java classes imported successfully")
print("Reference frame:", FramesFactory.getEME2000())
