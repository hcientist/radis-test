# https://radis.readthedocs.io/en/latest/#quick-start
from radis import calc_spectrum
import time
payload = {}

payload["min_wavenumber_range"] = 1900
payload["max_wavenumber_range"] = 2300
payload["species"] = [{"molecule": "CO", "mole_fraction": 0.1}]
payload["pressure"] = 1.01325
payload["tgas"] = 300
payload["tvib"] = None
payload["trot"] = None
payload["path_length"] = 1
payload["database"] = "hitran"

print("will calc")

# https://github.com/suzil/radis-app/blob/main/server/main.py#L43-L61
spectrum = calc_spectrum(
    payload["min_wavenumber_range"],
    payload["max_wavenumber_range"],
    molecule=[species["molecule"] for species in payload["species"]],
    mole_fraction={
        species["molecule"]: species["mole_fraction"] for species in payload["species"]
    },
    # TODO: Hard-coding "1,2,3" as the isotopologue for the time-being
    isotope={species["molecule"]: "1,2,3" for species in payload["species"]},
    pressure=payload["pressure"],
    Tgas=payload["tgas"],
    Tvib=payload["tvib"],
    Trot=payload["trot"],
    path_length=payload["path_length"],
    export_lines=False,
    wstep="auto",
    databank=payload["database"],
    use_cached=True,
)
print("did calc")
spectrum.apply_slit(0.5, "nm")  # simulate an experimental slit
print("applied")
spectrum.plot("radiance", show=True)
time.sleep(10)
print("plotted")
