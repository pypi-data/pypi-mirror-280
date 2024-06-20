import pytest
from test_results_parser import Outcome, Testrun, parse_junit_xml


class TestParsers:
    @pytest.mark.parametrize(
        "filename,expected",
        [
            (
                "./tests/junit.xml",
                [
                    Testrun(
                        "tests.test_parsers.TestParsers\x1ftest_junit[junit.xml--True]",
                        0.001,
                        Outcome.Failure,
                        "pytest",
                        """self = &lt;test_parsers.TestParsers object at 0x102182d10&gt;, filename = 'junit.xml', expected = '', check = True

    @pytest.mark.parametrize(
        "filename,expected,check",
        [("junit.xml", "", True), ("jest-junit.xml", "", False)],
    )
    def test_junit(self, filename, expected, check):
        with open(filename) as f:
            junit_string = f.read()
            res = parse_junit_xml(junit_string)
            print(res)
            if check:
&gt;               assert res == expected
E               AssertionError: assert [{'duration': '0.010', 'name': 'tests.test_parsers.TestParsers.test_junit[junit.xml-]', 'outcome': 'failure'}, {'duration': '0.063', 'name': 'tests.test_parsers.TestParsers.test_junit[jest-junit.xml-]', 'outcome': 'pass'}] == ''

tests/test_parsers.py:16: AssertionError""",
                    ),
                    Testrun(
                        "tests.test_parsers.TestParsers\x1ftest_junit[jest-junit.xml--False]",
                        0.064,
                        Outcome.Pass,
                        "pytest",
                        None,
                    ),
                ],
            ),
            (
                "./tests/jest-junit.xml",
                [
                    Testrun(
                        "Title when rendered renders pull title\x1fTitle when rendered renders pull title",
                        0.036,
                        Outcome.Pass,
                        "Title",
                        None,
                    ),
                    Testrun(
                        "Title when rendered renders pull author\x1fTitle when rendered renders pull author",
                        0.005,
                        Outcome.Pass,
                        "Title",
                        None,
                    ),
                    Testrun(
                        "Title when rendered renders pull updatestamp\x1fTitle when rendered renders pull updatestamp",
                        0.002,
                        Outcome.Pass,
                        "Title",
                        None,
                    ),
                    Testrun(
                        "Title when rendered for first pull request renders pull title\x1fTitle when rendered for first pull request renders pull title",
                        0.006,
                        Outcome.Pass,
                        "Title",
                        None,
                    ),
                ],
            ),
            (
                "./tests/vitest-junit.xml",
                [
                    Testrun(
                        "__tests__/test-file-1.test.ts\x1ffirst test file &gt; 2 + 2 should equal 4",
                        0.01,
                        Outcome.Failure,
                        "__tests__/test-file-1.test.ts",
                        """AssertionError: expected 5 to be 4 // Object.is equality
 ❯ __tests__/test-file-1.test.ts:20:28""",
                    ),
                    Testrun(
                        "__tests__/test-file-1.test.ts\x1ffirst test file &gt; 4 - 2 should equal 2",
                        0,
                        Outcome.Pass,
                        "__tests__/test-file-1.test.ts",
                        None,
                    ),
                ],
            ),
            (
                "./tests/empty_failure.junit.xml",
                [
                    Testrun(
                        "test.test\x1ftest.test works",
                        0.234,
                        Outcome.Pass,
                        "test",
                        None,
                    ),
                    Testrun(
                        "test.test\x1ftest.test fails",
                        1,
                        Outcome.Failure,
                        "test",
                        "TestError",
                    ),
                ],
            ),
        ],
    )
    def test_junit(self, filename, expected):
        with open(filename, "b+r") as f:
            res = parse_junit_xml(f.read())
            assert len(res) == len(expected)
            for restest, extest in zip(res, expected):
                assert restest == extest
