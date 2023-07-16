# install.packages("googledrive")
library(googledrive)
library(readxl)

# Uncomment next line if you need to authenticate
# googledrive::drive_auth()

google_sheet_to_df <- function(pattern) {
    # Example: find ID of a Google Sheet, by name
    google_sheet_ref <- googledrive::drive_find(
        type = "spreadsheet", 
        pattern = pattern)

    # Download file to local Excel file (saving to object local_file_ref)
    local_file_ref <- googledrive::drive_download(
        file = google_sheet_ref,
        overwrite = TRUE
    )
    
    # Save contents to df, and delete the local file
    df <- readxl::read_excel(local_file_ref$local_path)
    unlink(local_file_ref$local_path)

    # Read local file into data frame in memory
    return(df)
}

# Example
# df <- google_sheet_to_df(pattern = "Data - Salesforce Num Opportunities by Job Location Zipcode")