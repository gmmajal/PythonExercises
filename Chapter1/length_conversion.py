length=640 #given in meters
inches=(length*100.0)/2.54
feet= inches/12.0
yards= feet/3.0
british_miles=yards/1760

print 'A length of %g meters corresponds to %2f inches, %2f feet, %2f yards, or %2f miles.'%(length, inches, feet, yards, british_miles)
