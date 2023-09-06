#!/bin/bash
# This script downloads covid data and displays it

DATA=$(curl https://api.covidtracking.com/v1/us/current.json)
POSITIVE=$(echo $DATA | jq '.[0].positive')
NEGATIVE=$(echo $DATA | jq '.[0].negative')
TOTAL=$(echo $DATA | jq '.[0].totalTestResults')
PENDING=$(echo $DATA | jq '.[0].pending')
DEATHS=$(echo $DATA | jq '.[0].hospitalizedCumulative')
TODAY=$(date)

echo "On $TODAY, there were $POSITIVE positive COVID cases, $NEGATIVE negative results, $PENDING pending results, $TOTAL total results, and $DEATHS deaths."
