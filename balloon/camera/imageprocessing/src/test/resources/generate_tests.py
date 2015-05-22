from os import listdir, linesep, rename, makedirs
from os.path import isfile, join, abspath, exists, splitext

scenarios = open('scenarios.txt', 'r');
lines = scenarios.readlines();
scenarios.close();


testText = "#include \"gtest/gtest.h\"\n\n#include \"imageprocessor.hpp\"\n\nusing namespace imageprocessor;\n\nTEST(test_images, {TEST_NAME}) {\n    const Input *const input = new Input(\"{TEST_FILE}\");\n    const std::unique_ptr<const Result> result = imageprocessor::processImage(input);\n    ASSERT_EQ({EXPECTED_RESULT}, result->send);\n}\n"

directory = "../gen/cpp"
if not exists(directory):
    makedirs(directory)

for line in lines:
    splits = line.split('\t');
    imageName = splits[0];
    expected_result = splits[1];
    fileName = "hab-image-processing/" + imageName
    if(isfile(fileName)):
        fileName = abspath(fileName)
        imageNameWithoutExtension, extension = splitext(imageName)

        testCaseText = testText
        testCaseText = testCaseText.replace("{TEST_NAME}", imageNameWithoutExtension.replace("-","_"))
        testCaseText = testCaseText.replace("{TEST_FILE}", fileName)
        if(expected_result == '1'):
            testCaseText = testCaseText.replace("{EXPECTED_RESULT}", "true")
        else:
            testCaseText = testCaseText.replace("{EXPECTED_RESULT}", "false")

        testFile = open(directory + "/test_" + imageNameWithoutExtension + ".cpp", 'w')
        testFile.write(testCaseText)
        testFile.close()
