;; Auto-generated. Do not edit!


(when (boundp 'irig::IntArray)
  (if (not (find-package "IRIG"))
    (make-package "IRIG"))
  (shadow 'IntArray (find-package "IRIG")))
(unless (find-package "IRIG::INTARRAY")
  (make-package "IRIG::INTARRAY"))

(in-package "ROS")
;;//! \htmlinclude IntArray.msg.html


(defclass irig::IntArray
  :super ros::object
  :slots (_data ))

(defmethod irig::IntArray
  (:init
   (&key
    ((:data __data) (make-array 0 :initial-element 0 :element-type :integer))
    )
   (send-super :init)
   (setq _data __data)
   self)
  (:data
   (&optional __data)
   (if __data (setq _data __data)) _data)
  (:serialization-length
   ()
   (+
    ;; int32[] _data
    (* 4    (length _data)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; int32[] _data
     (write-long (length _data) s)
     (dotimes (i (length _data))
       (write-long (elt _data i) s)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; int32[] _data
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _data (instantiate integer-vector n))
     (dotimes (i n)
     (setf (elt _data i) (sys::peek buf ptr- :integer)) (incf ptr- 4)
     ))
   ;;
   self)
  )

(setf (get irig::IntArray :md5sum-) "563b27884d008b0d2adff54dc1f9e4f5")
(setf (get irig::IntArray :datatype-) "irig/IntArray")
(setf (get irig::IntArray :definition-)
      "int32[] data

")



(provide :irig/IntArray "563b27884d008b0d2adff54dc1f9e4f5")


