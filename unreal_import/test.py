import unreal

# RigVMBlueprint 생성
blueprint_name = "RigVMBlueprint_1"

# RigVMBlueprint 생성
rig_blueprint = unreal.RigVMBlueprint()

# 추가할 변수 이름 정의
variable_name = unreal.Name("taskname")

# 변수의 C++ 타입 정의 (예시로 FString 사용)
cpp_type = "FString"

# 변수 추가
added_variable = rig_blueprint.add_member_variable(variable_name, cpp_type)

# 추가한 변수의 확인을 위해 출력
print(f"Added variable '{added_variable}' to RigVMBlueprint.")

# RigVMBlueprint 저장 (옵션)
save_path = "/Game/Blueprints"  # 저장할 경로 지정
save_name = blueprint_name + "_generated"
rig_blueprint.save_package(save_path, save_name)

# 생성한 블루프린트 이름 출력
print(f"Generated RigVMBlueprint: {save_path}/{save_name}")




