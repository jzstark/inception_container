open Owl

let _ = 
  let img = Sys.argv.(1) in
  let labels = InceptionV3.infer img in 
  let labels_json   = InceptionV3.to_json   ~top:5 labels in 

  labels_json