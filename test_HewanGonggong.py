# ********RoostGPT********
"""
Test generated by RoostGPT for test python-oop-test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=gonggong_d441f1cd49
ROOST_METHOD_SIG_HASH=gonggong_b704fd9060


Scenario 1: Testing the Gonggong Function with Different Animal Objects
Details:
  TestName: test_gonggong_function_with_different_animals
  Description: This test is intended to verify the gonggong function when invoked with different animal objects. The purpose is to ensure that the function behaves consistently across different animal types.
Execution:
  Arrange: Initialize objects of different animal classes such as dog, wolf, and lion.
  Act: Invoke the gonggong function on these objects.
  Assert: The expected output should be 'Suara gonggongan hewan', irrespective of the animal type.
Validation:
  The test is important because it validates the consistency of the gonggong function. The expected result aligns with the function's specification that it should return the same sound regardless of the animal type.

Scenario 2: Testing the Gonggong Function with No Animal Object
Details:
  TestName: test_gonggong_function_with_no_animal
  Description: This test is intended to verify the behavior of the gonggong function when no animal object is passed. The purpose is to check if the function can handle such a scenario without breaking.
Execution:
  Arrange: No setup or animal object initialization is required for this test.
  Act: Invoke the gonggong function without passing an animal object.
  Assert: As per the function's specification, it should still return 'Suara gonggongan hewan'.
Validation:
  This test is important because it checks the robustness of the gonggong function. The function should be able to handle scenarios when no animal object is passed and still return the correct sound.

Scenario 3: Testing the Gonggong Function with Multiple Invocations
Details:
  TestName: test_gonggong_function_with_multiple_invocations
  Description: This test is intended to verify the behavior of the gonggong function when it is invoked multiple times consecutively. The purpose is to check if the function maintains its consistency over multiple calls.
Execution:
  Arrange: Initialize an animal object.
  Act: Invoke the gonggong function multiple times on the same animal object.
  Assert: Each invocation should return 'Suara gonggongan hewan'.
Validation:
  This test is important because it checks the consistency of the gonggong function over multiple invocations. The function should always return the same sound, regardless of the number of times it is called.
"""

# ********RoostGPT********
import pytest
from cth2 import Hewan, Anjing, Srigala, Singa

class Test_HewanGonggong:

    @pytest.mark.positive
    def test_gonggong_function_with_different_animals(self):
        # Arrange
        dog = Anjing('Anjing')
        wolf = Srigala('Serigala')
        lion = Singa('Singa')

        # Act
        dog_result = dog.gonggong()
        wolf_result = wolf.gonggong()
        lion_result = lion.gonggong()

        # Assert
        assert dog_result == 'Suara gonggongan hewan'
        assert wolf_result == 'Suara gonggongan hewan'
        assert lion_result == 'Suara gonggongan hewan'

    @pytest.mark.negative
    def test_gonggong_function_with_no_animal(self):
        # Arrange
        animal = Hewan()

        # Act
        result = animal.gonggong()

        # Assert
        assert result == 'Suara gonggongan hewan'

    @pytest.mark.regression
    def test_gonggong_function_with_multiple_invocations(self):
        # Arrange
        dog = Anjing('Anjing')

        # Act and Assert
        for _ in range(5):
            assert dog.gonggong() == 'Suara gonggongan hewan'
