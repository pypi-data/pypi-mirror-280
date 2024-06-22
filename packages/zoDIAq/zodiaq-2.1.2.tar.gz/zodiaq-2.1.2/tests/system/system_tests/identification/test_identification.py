import os
import pandas as pd
import numpy as np
import subprocess
from tempfile import TemporaryDirectory
import numpy as np
import pytest
import re
from pyteomics import mgf
import shutil

from tests.system.system_tests.identification import (
    create_template_library_dataframe,
    make_mgf_library_from_template_library_dataframe,
    spectrastColumns,
    BaselineSpectraBreakdown,
    NoMatchSpectraBreakdown,
    NoCompensationVoltageSpectraBreakdown,
    MatchToleranceSpectraBreakdown,
    CustomCorrectionSpectraBreakdown,
    StDevCorrectionSpectraBreakdown,
)


def get_parent_dir():
    return os.path.dirname(os.path.abspath(__file__))


def get_file_from_system_test_folder(file):
    return os.path.join(get_parent_dir(), "test_files", file)


def assert_pandas_dataframes_are_equal(expectedDf, df):
    for columnName in expectedDf.columns:
        assert columnName in df.columns
        expectedColumn = np.array(expectedDf[columnName])
        column = np.array(df[columnName])
        if expectedColumn.dtype.kind in np.typecodes["AllFloat"]:
            np.testing.assert_array_almost_equal(expectedColumn, column)
        else:
            np.testing.assert_array_equal(expectedColumn, column)


isSavingTestFiles = False


@pytest.fixture(scope="module")
def libraryTemplateDataFrame():
    return create_template_library_dataframe(
        minMz=400,
        maxMz=1600,
        precursorMzDiff=1,
        peakMzDiff=0.1,
        peakIntensityDiff=1000.0,
    )


@pytest.fixture(scope="module")
def systemTestFileDirectory():
    return TemporaryDirectory(prefix="zodiaq_identification_system_test_files_")


@pytest.fixture(scope="module")
def libraryFileDirectory(libraryTemplateDataFrame, systemTestFileDirectory):
    libraryDirectory = os.path.join(systemTestFileDirectory.name, "library_files")
    os.mkdir(libraryDirectory)
    libraryTemplateDataFrame.to_csv(
        os.path.join(libraryDirectory, "template_test_library.csv"), index=False
    )
    spectrastDataFrame = libraryTemplateDataFrame.copy()
    spectrastDataFrame.columns = spectrastColumns
    spectrastDataFrame.to_csv(
        os.path.join(libraryDirectory, "spectrast_test_library.csv"), index=False
    )
    mgfSpectra = make_mgf_library_from_template_library_dataframe(
        libraryTemplateDataFrame
    )
    mgf.write(mgfSpectra, os.path.join(libraryDirectory, "mgf_test_library.mgf"))
    return libraryDirectory


@pytest.fixture(scope="module")
def inputFileDirectory(systemTestFileDirectory):
    inputDirectory = os.path.join(systemTestFileDirectory.name, "input_files")
    os.mkdir(inputDirectory)
    return inputDirectory


@pytest.fixture(scope="module")
def expectedOutputDirectory(systemTestFileDirectory):
    expectedOutputDirectory = os.path.join(
        systemTestFileDirectory.name, "expected_output_files"
    )
    os.mkdir(expectedOutputDirectory)
    return expectedOutputDirectory


def test__identification__baseline_run__spectrast_library(
    libraryTemplateDataFrame,
    libraryFileDirectory,
    inputFileDirectory,
    expectedOutputDirectory,
):
    baselineSpectraBreakdown = BaselineSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader = "baseline_run_spectrast"
    baselineSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    baselineSpectraBreakdown.expectedOutputDf.to_csv(
        os.path.join(expectedOutputDirectory, f"{inputFileHeader}.csv"), index=False
    )
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
    ]
    subprocess.run(args, capture_output=True)
    outputDirContents = os.listdir(outputDir.name)
    assert len(outputDirContents) == 1
    zodiaqDir = os.path.join(outputDir.name, outputDirContents[0])
    zodiaqDirContents = os.listdir(zodiaqDir)
    assert len(zodiaqDirContents) == 1
    outputFile = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputDf = pd.read_csv(outputFile)
    outputDf = (
        outputDf.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    assert_pandas_dataframes_are_equal(
        baselineSpectraBreakdown.expectedOutputDf, outputDf
    )


def test__identification__baseline_run__mgf_library(
    libraryTemplateDataFrame,
    libraryFileDirectory,
    inputFileDirectory,
    expectedOutputDirectory,
):
    baselineSpectraBreakdown = BaselineSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader = "baseline_run_mgf"
    baselineSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "mgf_test_library.mgf")
    baselineSpectraBreakdown.expectedOutputDf.to_csv(
        os.path.join(expectedOutputDirectory, f"{inputFileHeader}.csv"), index=False
    )
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
    ]
    subprocess.run(args, capture_output=True)
    outputDirContents = os.listdir(outputDir.name)
    assert len(outputDirContents) == 1
    zodiaqDir = os.path.join(outputDir.name, outputDirContents[0])
    zodiaqDirContents = os.listdir(zodiaqDir)
    assert len(zodiaqDirContents) == 1
    outputFile = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputDf = pd.read_csv(outputFile)
    outputDf = (
        outputDf.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    assert_pandas_dataframes_are_equal(
        baselineSpectraBreakdown.expectedOutputDf, outputDf
    )


def test__identification__baseline__two_inputs_creates_two_outputs_independent_of_one_another(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    baselineSpectraBreakdown = BaselineSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader1 = "baseline_output_1"
    baselineSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader1
    )
    inputFileHeader2 = "baseline_output_2"
    baselineSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader2
    )
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    inputQueryFile1 = os.path.join(inputFileDirectory, f"{inputFileHeader1}.mzXML")
    inputQueryFile2 = os.path.join(inputFileDirectory, f"{inputFileHeader2}.mzXML")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile1,
        "-i",
        inputQueryFile2,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
    ]

    subprocess.run(args, capture_output=True)
    outputDirContents = os.listdir(outputDir.name)
    assert len(outputDirContents) == 1
    zodiaqDir = os.path.join(outputDir.name, outputDirContents[0])
    zodiaqDirContents = os.listdir(zodiaqDir)
    assert len(zodiaqDirContents) == 2
    outputFile1 = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputFile2 = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputDf1 = pd.read_csv(outputFile1)
    outputDf2 = pd.read_csv(outputFile2)
    outputDf1 = (
        outputDf1.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    outputDf2 = (
        outputDf2.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    assert_pandas_dataframes_are_equal(
        baselineSpectraBreakdown.expectedOutputDf, outputDf1
    )
    assert outputDf1.equals(outputDf2)


def test__identification__baseline_no_matches_raises_error(
    libraryTemplateDataFrame,
    libraryFileDirectory,
    inputFileDirectory,
    expectedOutputDirectory,
):
    noMatchSpectraBreakdown = NoMatchSpectraBreakdown(libraryTemplateDataFrame)
    noMatchFileHeader = "no_match_input"
    noMatchSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, noMatchFileHeader
    )
    baselineSpectraBreakdown = BaselineSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader = "match_input"
    baselineSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    noMatchQueryFile = os.path.join(inputFileDirectory, f"{noMatchFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    baselineSpectraBreakdown.expectedOutputDf.to_csv(
        os.path.join(expectedOutputDirectory, f"{inputFileHeader}.csv"), index=False
    )
    noMatchSpectraBreakdown.expectedOutputDf.to_csv(
        os.path.join(expectedOutputDirectory, f"{noMatchFileHeader}.csv"), index=False
    )
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    assert_no_matches_before_correction_raises_warning_and_skips_offending_file_only(
        inputQueryFile,
        noMatchQueryFile,
        libraryFile,
        outputDir,
        baselineSpectraBreakdown,
    )


def assert_no_matches_before_correction_raises_warning_and_skips_offending_file_only(
    inputQueryFile, noMatchQueryFile, libraryFile, outputDir, baselineSpectraBreakdown
):
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-i",
        noMatchQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
    ]
    errorOutput = f"No matches found between library and query spectra. Skipping {noMatchQueryFile} file."
    output = subprocess.run(args, capture_output=True)
    assert errorOutput in str(output.stderr)
    outputDirContents = os.listdir(outputDir.name)
    assert len(outputDirContents) == 1
    zodiaqDir = os.path.join(outputDir.name, outputDirContents[0])
    zodiaqDirContents = os.listdir(zodiaqDir)
    assert len(zodiaqDirContents) == 1
    outputFile = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputDf = pd.read_csv(outputFile)
    outputDf = (
        outputDf.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    assert_pandas_dataframes_are_equal(
        baselineSpectraBreakdown.expectedOutputDf, outputDf
    )


def assert_no_matches_after_correction_raises_warning(
    inputQueryFile, libraryFile, outputDir, baselineSpectraBreakdown
):
    """
    Currently unused. The applicability of this error is questionable and may be removed entirely in the future.

    Would be added to 'test__identification__baseline_no_matches_raises_error', though it would require using
        input data with wider differences between m/z values in each spectra.
    '''
    assert_no_matches_after_correction_raises_warning(
        inputQueryFile, libraryFile, outputDir, baselineSpectraBreakdown
    )
    '''
    """
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
    ]
    errorOutput = f"No matches found between library and query spectra. Skipping {inputQueryFile} file."
    output = subprocess.run(args, capture_output=True)
    assert errorOutput in str(output.stderr)


def test__identification__no_compensation_voltage_succeeds(
    libraryTemplateDataFrame,
    libraryFileDirectory,
    inputFileDirectory,
    expectedOutputDirectory,
):
    noCompensationVoltageSpectraBreakdown = NoCompensationVoltageSpectraBreakdown(
        libraryTemplateDataFrame
    )
    inputFileHeader = "no_compensation_voltage"
    noCompensationVoltageSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    noCompensationVoltageSpectraBreakdown.expectedOutputDf.to_csv(
        os.path.join(expectedOutputDirectory, f"{inputFileHeader}.csv"), index=False
    )
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
    ]
    subprocess.run(args, capture_output=True)
    outputDirContents = os.listdir(outputDir.name)
    assert len(outputDirContents) == 1
    zodiaqDir = os.path.join(outputDir.name, outputDirContents[0])
    zodiaqDirContents = os.listdir(zodiaqDir)
    assert len(zodiaqDirContents) == 1
    outputFile = os.path.join(zodiaqDir, zodiaqDirContents[0])
    outputDf = pd.read_csv(outputFile)
    outputDf = (
        outputDf.drop(["fileName"], axis=1)
        .sort_values(["cosine", "MzLIB"], ascending=[False, True])
        .reset_index(drop=True)
    )
    assert_pandas_dataframes_are_equal(
        noCompensationVoltageSpectraBreakdown.expectedOutputDf, outputDf
    )


def test__identification__match_tolerance_excludes_values_that_exceed_ppm_value__one_peak_exclusion(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    matchToleranceSpectraBreakdown = MatchToleranceSpectraBreakdown(
        libraryTemplateDataFrame
    )
    inputFileHeader = "match_tolerance_one_peak"
    matchToleranceSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
        "-t",
        "29",
    ]
    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    outputFile = os.path.join(zodiaqDir, os.listdir(zodiaqDir)[0])
    outputDf = pd.read_csv(outputFile)
    matchedPeakNum = list(set(outputDf["shared"]))
    assert len(matchedPeakNum) == 1
    assert matchedPeakNum[0] == 9


def test__identification__match_tolerance_excludes_values_that_exceed_ppm_value__two_peak_exclusion(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    matchToleranceSpectraBreakdown = MatchToleranceSpectraBreakdown(
        libraryTemplateDataFrame
    )
    inputFileHeader = "match_tolerance_two_peaks"
    matchToleranceSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-nc",
        "-t",
        "28",
    ]
    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    outputFile = os.path.join(zodiaqDir, os.listdir(zodiaqDir)[0])
    outputDf = pd.read_csv(outputFile)
    matchedPeakNum = list(set(outputDf["shared"]))
    assert len(matchedPeakNum) == 1
    assert matchedPeakNum[0] == 8


def test__identification__custom_correction_creates_expected_number_of_matched_peaks(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    customCorrectionSpectraBreakdown = CustomCorrectionSpectraBreakdown(
        libraryTemplateDataFrame
    )
    inputFileHeader = "custom_correction"
    customCorrectionSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
    ]

    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    assert len(os.listdir(zodiaqDir)) == 1
    outputFile = os.path.join(zodiaqDir, os.listdir(zodiaqDir)[0])
    outputDf = pd.read_csv(outputFile)
    matchedPeakNum = list(set(outputDf["shared"]))
    assert len(matchedPeakNum) == 1
    assert matchedPeakNum[0] == 8


def test__identification__hist_flag_creates_histogram_image(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    customCorrectionSpectraBreakdown = CustomCorrectionSpectraBreakdown(
        libraryTemplateDataFrame
    )
    inputFileHeader = "histogram"
    customCorrectionSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-hist",
    ]

    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    assert len(os.listdir(zodiaqDir)) == 2
    extensions = [os.path.splitext(file)[1] for file in os.listdir(zodiaqDir)]
    assert ".png" in extensions


def test__identification__correction_with_first_standard_deviation_creates_expected_number_of_matched_peaks(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    stDevSpectraBreakdown = StDevCorrectionSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader = "standard_devation_1"
    stDevSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-c",
        "1",
    ]
    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    outputFile = os.path.join(zodiaqDir, os.listdir(zodiaqDir)[0])
    outputDf = pd.read_csv(outputFile)
    matchedPeakMean = np.mean(outputDf["shared"])
    assert matchedPeakMean > 6.62 and matchedPeakMean < 7.02


def test__identification__correction_with_second_standard_deviation_creates_expected_number_of_matched_peaks(
    libraryTemplateDataFrame, libraryFileDirectory, inputFileDirectory
):
    stDevSpectraBreakdown = StDevCorrectionSpectraBreakdown(libraryTemplateDataFrame)
    inputFileHeader = "standard_devation_2"
    stDevSpectraBreakdown.write_query_scan_data_input_files(
        inputFileDirectory, inputFileHeader
    )
    inputQueryFile = os.path.join(inputFileDirectory, f"{inputFileHeader}.mzXML")
    libraryFile = os.path.join(libraryFileDirectory, "spectrast_test_library.csv")
    outputDir = TemporaryDirectory(prefix="zodiaq_system_test")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        libraryFile,
        "-o",
        outputDir.name,
        "-c",
        "2",
    ]
    subprocess.run(args, capture_output=True)
    zodiaqDir = os.path.join(outputDir.name, os.listdir(outputDir.name)[0])
    outputFile = os.path.join(zodiaqDir, os.listdir(zodiaqDir)[0])
    outputDf = pd.read_csv(outputFile)
    matchedPeakMean = np.mean(outputDf["shared"])
    assert matchedPeakMean > 9.34 and matchedPeakMean < 9.74


@pytest.mark.skip(
    "future development may include improving the memory efficiency of the program. This function serves as a baseline for such tests."
)
def test__identification__stress_test_memory():
    denseLibraryDf = create_template_library_dataframe(
        minMz=100,
        maxMz=10000,
        precursorMzDiff=0.1,
        peakMzDiff=0.01,
        peakIntensityDiff=1000.0,
    )
    stDevSpectraBreakdown = StDevCorrectionSpectraBreakdown(denseLibraryDf)
    inputFileHeader = "stress_test"
    inputDir = TemporaryDirectory(prefix="zodiaq_system_stress_test_input")
    stDevSpectraBreakdown.write_query_scan_data_input_files(
        inputDir.name, inputFileHeader
    )
    inputQueryFile = os.path.join(inputDir.name, f"{inputFileHeader}.mzXML")
    libraryFileDirectory = TemporaryDirectory(
        prefix="zodiaq_system_stress_test_library"
    )
    denseLibraryDf.columns = spectrastColumns
    denseLibraryDf.to_csv(
        os.path.join(libraryFileDirectory.name, "spectrast_stress_test_lib.csv")
    )
    outputDir = TemporaryDirectory(prefix="zodiaq_system_stress_test_output")
    args = [
        "zodiaq",
        "id",
        "-i",
        inputQueryFile,
        "-l",
        os.path.join(libraryFileDirectory.name, "spectrast_stress_test_lib.csv"),
        "-o",
        outputDir.name,
    ]
    subprocess.run(args)


@pytest.mark.skip(
    "Test files are temporarily made on-the-fly, but there are instances where one would want to investigate specific file outputs. This test function saves the test files to a permanent directory. Remove the skip tag if you want to save the files for in-depth data interrogation."
)
def test__identification__make_permanent_copy_of_test_files(systemTestFileDirectory):
    parentDir = os.path.dirname(systemTestFileDirectory.name)
    permanentTestDirectory = os.path.join(parentDir, "zodiaq_system_test_files")
    shutil.copytree(systemTestFileDirectory.name, permanentTestDirectory)
    print(f"\nsaved test files to {permanentTestDirectory}")
