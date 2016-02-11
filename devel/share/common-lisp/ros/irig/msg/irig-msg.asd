
(cl:in-package :asdf)

(defsystem "irig-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "IntArray" :depends-on ("_package_IntArray"))
    (:file "_package_IntArray" :depends-on ("_package"))
  ))