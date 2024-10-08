def process():
    import cv2
    from pyzbar.pyzbar import decode
    from pydub import AudioSegment
    from pydub.playback import play
    from student_db import ai_data,others_data
    
    # Load beep sound

    song = AudioSegment.from_wav("C:\\Users\\DELL\\Desktop\\Project\\python\\beep.wav")

    # Open the default camera (camera index 0)
    #cap = cv2.VideoCapture('http://192.168.43.1:8080/video')
    #cap = cv2.VideoCapture('http://192.168.182.156:8080/video')
    #cap = cv2.VideoCapture('http://10.136.224.80:8080/video')
    cap = cv2.VideoCapture('http://100.70.33.142:8080/video')
    cap.set(3, 600)  # Width
    cap.set(4, 400)  # Height

    # Set the desired display width and height
    display_width = 800
    display_height = 600

    last_detected_barcode = []

    while True:
        # Capture a frame from the camera
        success, frame = cap.read()

        # Check if the frame was successfully captured
        if not success:
            print("Error: Failed to capture a frame")
            break

        # Flip the image like a mirror image
        frame = cv2.flip(frame, 1)

        # Decode barcodes in the frame
        detected_barcodes = decode(frame)

        # If no barcode detected
        if not detected_barcodes:
            None
            

        # If barcode detected
        else:
            # Loop through detected barcodes
            for barcode in detected_barcodes:
                # If barcode is not blank
                if barcode.data != "":
                    cv2.putText(frame, str(barcode.data), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 2)
                    play(song)
                    # cv2.imwrite("code.png", frame)
                    last_detected_barcode.append(int(barcode.data))
                    break

        # Resize the frame for display
        resized_frame = cv2.resize(frame, (display_width, display_height))

        # Display the resized result
        cv2.imshow('Barcode Scanner', resized_frame)
        if last_detected_barcode:
            break
        # Exit when 'q' is pressed
        key = cv2.waitKey(1)
        if key == ord('q'):
            break

    # Release the camera capture object and close the window
    cap.release()
    cv2.destroyAllWindows()

    # Print the last detected barcode value when the loop is stopped
    if last_detected_barcode:
        data=last_detected_barcode[0]
        input_data=str(data)
        split_data=input_data[:9]
        register_num=721921243
        if register_num==int(split_data):
            ai_data(data)
             
        else:
            others_data(data)
             
    else:
        print("No barcodes were detected.")



