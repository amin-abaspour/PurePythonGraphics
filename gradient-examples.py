
# save_bmp(
#     "./output/linear_gradient.bmp",
#     rgb_matrix_to_bmp(
#         linear_gradient(
#             400,  # Width of the image
#             400,  # Height of the image
#             (0, 0, 255),  # Start color
#             (255, 0, 0),  # End color
#             45  # Angle in degrees
#         )
#     )
# )

# save_bmp(
#     "./output/radial_gradient.bmp",
#     rgb_matrix_to_bmp(
#         radial_gradient(
#             400,  # Width of the image
#             400,  # Height of the image
#             (200, 200),  # Center of the gradient (x, y)
#             300,  # Radius of the gradient
#             (255, 0, 0),  # Start color (Green)
#             (0, 0, 255)  # End color (Blue)
#         )
#     )
# )

# save_bmp(
#     "./output/conic_gradient.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             width=400,
#             height=400,
#             center=(200, 200),
#             color_stops=[
#                 (0,   (255, 0, 0)),  # Red at angle=0
#                 (360, (0, 0, 255))   # Blue at angle=360
#             ],
#             angle_offset=90
#         )
#     )
# )

# save_bmp(
#     "./output/conic_rainbow.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             width=400,
#             height=400,
#             center=(200, 200),
#             color_stops=[
#                 (0,   (255,   0,   0)),  # Red
#                 (60,  (255, 255,   0)),  # Yellow
#                 (120, (0,   255,   0)),  # Green
#                 (180, (0,   255, 255)),  # Cyan
#                 (240, (0,     0, 255)),  # Blue
#                 (300, (255,   0, 255)),  # Magenta
#                 (360, (255,   0,   0))   # Back to Red
#             ],
#             angle_offset=0
#         )
#     )
# )


# save_bmp(
#     "./output/conic_three_sharp.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             400, 400, (200, 200),
#             [
#                 (0,         (255,   0,   0)),   # Red start
#                 (119.9999,  (255,   0,   0)),   # Still Red up to just before 120°
#                 (120,       (255, 255,   0)),   # Sharp jump to Yellow at 120°
#                 (239.9999,  (255, 255,   0)),   # Yellow continues
#                 (240,       (0,   255,   0)),   # Sharp jump to Green at 240°
#                 (359.9999,  (0,   255,   0)),   # Green continues
#                 (360,       (255,   0,   0))    # Back to Red at 360°
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/conic_four_sharp.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             400, 400, (200, 200),
#             [
#                 (0,        (255,   0,   0)),  # Red
#                 (89.9999,  (255,   0,   0)),
#                 (90,       (255, 255,   0)),  # Sharp jump to Yellow
#                 (179.9999, (255, 255,   0)),
#                 (180,      (0,   255,   0)),  # Sharp jump to Green
#                 (269.9999, (0,   255,   0)),
#                 (270,      (0,     0, 255)),  # Sharp jump to Blue
#                 (359.9999, (0,     0, 255)),
#                 (360,      (255,   0,   0))   # Back to Red
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/conic_starburst_gradient.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             width=400,
#             height=400,
#             center=(200, 200),
#             color_stops=[
#                 (0,   (180, 230, 255)),  # Light cyan
#                 (30,  (120, 180, 220)),  # Slightly darker
#                 (60,  (180, 230, 255)),  # Light again
#                 (90,  (120, 180, 220)),
#                 (120, (180, 230, 255)),
#                 (150, (120, 180, 220)),
#                 (180, (180, 230, 255)),
#                 (210, (120, 180, 220)),
#                 (240, (180, 230, 255)),
#                 (270, (120, 180, 220)),
#                 (300, (180, 230, 255)),
#                 (330, (120, 180, 220)),
#                 (360, (180, 230, 255))   # Close loop
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/conic_starburst_sharp.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             400, 400, (200, 200),
#             [
#                 # Light blue wedge
#                 (0,       (150, 200, 255)),
#                 (29.9999, (150, 200, 255)),
#                 (30,      (100, 150, 200)),  # Darker blue wedge
#                 (59.9999, (100, 150, 200)),
#                 (60,      (150, 200, 255)),  # Light again
#                 (89.9999, (150, 200, 255)),
#                 (90,      (100, 150, 200)),
#                 (119.9999,(100, 150, 200)),
#                 (120,     (150, 200, 255)),
#                 (149.9999,(150, 200, 255)),
#                 (150,     (100, 150, 200)),
#                 (179.9999,(100, 150, 200)),
#                 (180,     (150, 200, 255)),
#                 (209.9999,(150, 200, 255)),
#                 (210,     (100, 150, 200)),
#                 (239.9999,(100, 150, 200)),
#                 (240,     (150, 200, 255)),
#                 (269.9999,(150, 200, 255)),
#                 (270,     (100, 150, 200)),
#                 (299.9999,(100, 150, 200)),
#                 (300,     (150, 200, 255)),
#                 (329.9999,(150, 200, 255)),
#                 (330,     (100, 150, 200)),
#                 (359.9999,(100, 150, 200)),
#                 (360,     (150, 200, 255)) # Close loop
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/conic_checkerboard.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             400, 400, (200, 200),
#             [
#                 (0,        (255,255,255)),  # White
#                 (45,       (255,255,255)),
#                 (45.0001,  (0,0,0)),        # Black
#                 (90,       (0,0,0)),
#                 (90.0001,  (255,255,255)),  # White
#                 (135,      (255,255,255)),
#                 (135.0001, (0,0,0)),        # Black
#                 (180,      (0,0,0)),
#                 (180.0001, (255,255,255)),  # White
#                 (225,      (255,255,255)),
#                 (225.0001, (0,0,0)),        # Black
#                 (270,      (0,0,0)),
#                 (270.0001, (255,255,255)),  # White
#                 (315,      (255,255,255)),
#                 (315.0001, (0,0,0)),        # Black
#                 (360,      (0,0,0))         # Wrap to Black
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/conic_blocks.bmp",
#     rgb_matrix_to_bmp(
#         conic_gradient(
#             width=400,
#             height=400,
#             center=(100, 100),
#             color_stops=[
#                 (0,       (0, 0, 0)),         # Black start
#                 (89.9999, (0, 0, 0)),         # Black up to just before 90°
#                 (90,      (255, 255, 255)),   # Switch to White at 90°
#                 (179.9999,(255, 255, 255)),   # White until just before 180°
#                 (180,     (0, 0, 0)),         # Switch to Black at 180°
#                 (269.9999,(0, 0, 0)),         # Black until just before 270°
#                 (270,     (255, 255, 255)),   # Switch to White at 270°
#                 (359.9999,(255, 255, 255)),   # White until just before 360°
#                 (360,     (0, 0, 0))          # Back to Black at 360°
#             ],
#             angle_offset=0
#         )
#     )
# )

# save_bmp(
#     "./output/angular_gradient.bmp",
#     rgb_matrix_to_bmp(
#         angular_gradient(
#             400,  # Width of the image
#             400,  # Height of the image
#             (200, 200),  # Center of the gradient (x, y)
#             (255, 0, 0),  # Start color (Red)
#             (0, 0, 255)  # End color (Blue)
#         )
#     )
# )