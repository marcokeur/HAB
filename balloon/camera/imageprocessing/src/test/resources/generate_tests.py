from os import listdir, linesep, rename, makedirs
from os.path import isfile, join, abspath, exists, splitext

scenarios = open('scenarios.txt', 'r');
lines = scenarios.readlines();
scenarios.close();

testHeader = "#include \"gtest/gtest.h\"\n\n#include \"imageprocessor.hpp\"\n\nusing namespace imageprocessor;\n"

testText = "\nTEST(test_images, {TEST_NAME}) {\n    const Input *const input = new Input(\"{TEST_FILE}\");\n    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);\n    ASSERT_{EXPECTED_RESULT}(result->send);\n}\n"

directory = "../gen/cpp"
if not exists(directory):
    makedirs(directory)

for line in lines:
    splits = line.split('\t');
    imageName = splits[0];
    expected_result = splits[1].strip();
    fileName = "hab-image-processing/" + imageName
    if(isfile(fileName)):
        fileName = abspath(fileName)
        imageNameWithoutExtension, extension = splitext(imageName)

        testCaseText = testText
        testCaseText = testCaseText.replace("{TEST_NAME}", imageNameWithoutExtension.replace("-","_"))
        testCaseText = testCaseText.replace("{TEST_FILE}", fileName)

        if(expected_result == "1"):
            testCaseText = testCaseText.replace("{EXPECTED_RESULT}", "TRUE")
        else:
            testCaseText = testCaseText.replace("{EXPECTED_RESULT}", "FALSE")

        testFile = open(directory + "/test_" + imageNameWithoutExtension + ".cpp", 'w')
        testFile.write(testHeader)
        testFile.write(testCaseText)
        testFile.close()
