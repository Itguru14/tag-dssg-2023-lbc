library(tidyverse)
library(sf)
library(tigris)
library(readxl)
library(leaflet)

source("utilities/google_sheet_to_df.R")

df_zip <- zctas(year = 2020, cb = TRUE)

df <- google_sheet_to_df(pattern = "Data - Salesforce Num Opportunities by Job Location Zipcode")
names(df) <- c("zip", "num_opp")

df_map <- left_join(df, df_zip, by = join_by(zip == ZCTA5CE20))
df_map_sf <- st_sf(geometry = df_map$geometry) %>%
  st_transform(crs = st_crs(4326))

pal <- colorBin(
  palette = "viridis",
  domain = unique(df_map$num_opp),
  bins = c(0, 1, 5, 10, 20, 100, Inf))

zipcode_map <- leaflet() %>%
  addTiles() %>%
  addPolygons(
    data = df_map_sf,
    fillColor = ~pal(df_map$num_opp),
    fillOpacity = 0.7,
    color = "#000000",
    weight = 1,
    label = ~paste("Zip code:", df_map$zip, "Count:", df_map$num_opp)
  ) %>%
  addLegend(pal = pal, values = unique(df_map$num_opp))

library(htmlwidgets)
saveWidget(zipcode_map, file = "analysis/zipcode_map/sf_opp__atl_zipcode_map.html")
