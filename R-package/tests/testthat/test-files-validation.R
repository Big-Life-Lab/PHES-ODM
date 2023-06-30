test_that("standard run with no issues", {
  expect_no_condition(create_release_files(1,1,"../../data/test-data/standard"))
})
test_that("warning with incorrect filetype", {
  expect_warning(create_release_files(1,1,"../../data/test-data/generate-warnings"),"ExistInSets")
})
