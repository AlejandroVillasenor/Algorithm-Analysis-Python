"""
Created on Sep 23 2023
Tarea 5. Filtro de tiktok

"""
import cv2 as cv
cascPath = "facedetector.xml"
faceCascade = cv.CascadeClassifier(cascPath)
face_filter = cv.imread("JASONMASK.png",cv.IMREAD_UNCHANGED)

#Dimensionones de la imagen de la mascara: 615, 615

#obtener acceso a la webcam
video_capture = cv.VideoCapture(0,cv.CAP_V4L)
anterior = 0
if not video_capture.isOpened():
        print('No se pudo acceder a la camara')
else:
    while True:
        #revisar si ya puedo leer imagenes de la camara
        ret, frame = video_capture.read()
        frame=cv.flip(frame,1)
        imagenGrises = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
        faces = faceCascade.detectMultiScale(
            imagenGrises,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30)
        )
        #por cada cara detectada colorcar un filtro
        for (x, y, w, h) in faces:
            face_x = x - 10# Aumentar la posición horizontal
            face_y = y - 20# Aumentar la posición vertical
            face_w = w + 30# Aumentar el tamaño horizontal
            face_h = h + 30 # Aumentar el tamaño vertical

            # Asegurarse de que el filtro facial no se salga de los límites de la imagen
            face_x = max(0, face_x)
            face_y = max(0, face_y)

            # Redimensionar el filtro facial
            scaled_face = cv.resize(face_filter, (face_w, face_h))

            # Superponer el filtro facial en la imagen
            for i in range(face_h):
                for j in range(face_w):
                    if 0 <= face_y + i < frame.shape[0] and 0 <= face_x + j < frame.shape[1] and scaled_face[i, j][3] != 0: 
                        for c in range(0, 3):
                            frame[face_y + i, face_x + j, c] = scaled_face[i, j, c]

        cv.imshow('Jason Mask', frame)
        #se motraran las caras mientra no presionemos la tecla q
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    #liberar la camara
    video_capture.release()
    #cerrar todas las ventanas
    cv.destroyAllWindows()

