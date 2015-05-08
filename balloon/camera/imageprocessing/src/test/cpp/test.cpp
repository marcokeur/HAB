#include "gtest/gtest.h"

TEST(test_images, test_images)
{
	ASSERT_EQ(0, 1);
}


int main (int argc, char** argv) {
	::testing::InitGoogleTest(&argc, argv);
	return RUN_ALL_TESTS();
}