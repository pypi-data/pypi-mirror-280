import os
import pytest
import numpy as np
from astropy.table import Table, QTable
import astropy.units as u
from molecularprofiles.molecularprofiles import MolecularProfile

# Define the path to the test data directory
TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test_data")


@pytest.fixture
def empty_mol_profile():
    # Define the path to the test grib file
    grib_file_path = os.path.join(TEST_DATA_DIR, "grib/sample.grib")
    # Create and return the MolecularProfile instance
    return MolecularProfile(grib_file_path)


@pytest.fixture
def mol_profile(empty_mol_profile):
    empty_mol_profile.get_data()
    return empty_mol_profile


def test_get_data(empty_mol_profile):
    # Test get_data method
    empty_mol_profile.get_data()
    # Perform assertions
    assert empty_mol_profile.data is not None
    assert empty_mol_profile.stat_data is not None
    assert empty_mol_profile.stat_description is not None
    assert isinstance(empty_mol_profile.data, Table)
    with pytest.raises(FileNotFoundError):
        t_mol_profile = MolecularProfile("/foo/bar/baz.grib")
        t_mol_profile.get_data()


def test_write_atmospheric_profile(mol_profile):
    # Define test parameters
    outfile = "test_atmospheric_profile.ecsv"
    outfile_bad = "test_atmospheric_profile.txt"
    co2_concentration = 415  # Placeholder value
    reference_atmosphere = None  # Placeholder value
    # Test write_atmospheric_profile method
    with pytest.raises(SystemExit):
        mol_profile.write_atmospheric_profile(
            outfile_bad, co2_concentration, reference_atmosphere
        )
    mol_profile.write_atmospheric_profile(
        outfile, co2_concentration, reference_atmosphere
    )
    # Perform assertions
    assert os.path.isfile(outfile)


def test_create_mdp(mol_profile):
    # Define test parameters
    mdp_file = "test_mdp_file.ecsv"
    # Test create_mdp method
    mol_profile.create_mdp(mdp_file)
    # Perform assertions
    assert os.path.isfile(mdp_file)


def test_rayleigh_extinction(mol_profile):
    # Define test parameters
    rayleigh_extinction_file = "test_rayleigh_extinction_file.ecsv"
    co2_concentration = 415  # Placeholder value
    wavelength_min = u.Quantity(340, unit="nm")  # Placeholder value
    wavelength_max = u.Quantity(360, unit="nm")  # Placeholder value
    # Test rayleigh_extinction method
    mol_profile.rayleigh_extinction(
        rayleigh_extinction_file,
        co2_concentration,
        wavelength_min,
        wavelength_max,
    )
    # Perform assertions
    assert os.path.isfile(rayleigh_extinction_file)


def test_convert_to_simtel_compatible(mol_profile):
    # Define test parameters
    input_ecsv_file = os.path.join(
        TEST_DATA_DIR, "ecsv/test_rayleigh_extinction_file.ecsv"
    )
    output_file = "test_rayleigh_extinction_profile_simtel.txt"
    observation_altitude = u.Quantity(5000, unit="m")
    # Test convert_to_simtel_compatible method
    mol_profile.convert_to_simtel_compatible(
        input_ecsv_file, output_file, observation_altitude
    )
    # Perform assertions
    assert os.path.isfile(output_file)


def test_timeseries_analysis(mol_profile):
    # Define test parameters
    outfile = "test_timeseries_analysis.ecsv"
    t_floor = u.Quantity(1000, unit="m")
    t_ceiling = u.Quantity(20000, unit="m")
    altitude_level = u.Quantity(2200, unit="m")
    atmospheric_parameter = "Temperature"
    # Test timeseries_analysis method
    mol_profile.timeseries_analysis(
        outfile,
        altitude_level=altitude_level,
        atmospheric_parameter=atmospheric_parameter,
        m_floor=t_floor,
        m_ceiling=t_ceiling,
    )
    # Perform assertions
    assert os.path.isfile(outfile)


def test_molecular_extinction(mol_profile):
    # Define test parameters
    mep_file = "molecular_extinction_file.ecsv"
    ozone_file_path = os.path.join(TEST_DATA_DIR, "ozone_tests/sample_ozone.grib")
    reference_atmosphere_file_path = os.path.join(
        TEST_DATA_DIR,
        "reference_atmospheres_tests/reference_atmo_model_v0_CTA-south_winter.ecsv",
    )
    rayleigh_extinction_file = "test_rayleigh_extinction_file.ecsv"
    ozone_cross_section_file = os.path.join(
        TEST_DATA_DIR,
        "ozone_tests/cross_sections/ozone_absorption_cross_section_digitised.ecsv",
    )
    co2_concentration = 415  # Placeholder value
    wavelength_min = u.Quantity(340, unit="nm")  # Placeholder value
    wavelength_max = u.Quantity(360, unit="nm")  # Placeholder value
    rayleigh_extinction_file = mol_profile.rayleigh_extinction(
        rayleigh_extinction_file,
        co2_concentration,
        wavelength_min,
        wavelength_max,
        reference_atmosphere=reference_atmosphere_file_path,
        rayleigh_scattering_altitude_bins=(
            2.158,
            2.208,
            2.258,
            2.358,
            2.458,
            2.658,
            2.858,
            3.158,
            3.658,
            4.158,
            4.5,
            5.0,
            5.5,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
            13.0,
            14.0,
            15.0,
            16.0,
            18.0,
            20.0,
            22.0,
            24.0,
            26.0,
            28.0,
            30.0,
            32.5,
            35.0,
            37.5,
            40.0,
            45.0,
            50.0,
            55.0,
            60.0,
            65.0,
            70.0,
            75.0,
            80.0,
            85.0,
            90.0,
            95.0,
            100.0,
            105.0,
            110.0,
            115.0,
            120.0,
        )
        * u.km,
    )
    rs_table = QTable.read(rayleigh_extinction_file, format="ascii")
    ozone_extinction_table = mol_profile.ozone_absorption(
        ozone_cross_section_file,
        wavelength_min,
        wavelength_max,
        rayleigh_scattering_altitude_bins=(
            2.158,
            2.208,
            2.258,
            2.358,
            2.458,
            2.658,
            2.858,
            3.158,
            3.658,
            4.158,
            4.5,
            5.0,
            5.5,
            6.0,
            7.0,
            8.0,
            9.0,
            10.0,
            11.0,
            12.0,
            13.0,
            14.0,
            15.0,
            16.0,
            18.0,
            20.0,
            22.0,
            24.0,
            26.0,
            28.0,
            30.0,
            32.5,
            35.0,
            37.5,
            40.0,
            45.0,
            50.0,
            55.0,
            60.0,
            65.0,
            70.0,
            75.0,
            80.0,
            85.0,
            90.0,
            95.0,
            100.0,
            105.0,
            110.0,
            115.0,
            120.0,
        )
        * u.km,
    )
    mep = mol_profile.molecular_extinction_profile(
        rayleigh_extinction_file, ozone_extinction_table, mep_file
    )
    # mep.write(outfile, overwrite=True)
    assert os.path.isfile(mep_file)
