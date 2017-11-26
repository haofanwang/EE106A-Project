
(cl:in-package :asdf)

(defsystem "my_chatter-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :std_msgs-msg
)
  :components ((:file "_package")
    (:file "JointState" :depends-on ("_package_JointState"))
    (:file "_package_JointState" :depends-on ("_package"))
  ))