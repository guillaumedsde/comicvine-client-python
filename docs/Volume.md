# Volume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique ID for the entity. | 
**name** | **str** | Name for the entity | [optional] 
**aliases** | **str** | List of aliases the entity is known by. A \\n (newline) seperates each alias. | [optional] 
**api_detail_url** | **str** | URL pointing to the entity detail resource. | [optional] 
**description** | **str** | Description of the entity. | [optional] 
**deck** | **str** | Brief summary of the Entity. | [optional] 
**site_detail_url** | **str** | URL pointing to the concept on Giant Bomb. | [optional] 
**date_added** | **str** | Date the entity was added to Comic Vine. | [optional] 
**date_last_updated** | **str** | Date the entity was last updated on Comic Vine. | [optional] 
**image** | [**Image**](Image.md) |  | [optional] 
**characters** | **list[object]** | A list of characters that appear in this volume. | [optional] 
**concepts** | **list[object]** | A list of concepts that appear in this volume. | [optional] 
**count_of_issues** | **int** | Number of issues included in this volume. | [optional] 
**first_issue** | [**Issue**](Issue.md) |  | [optional] 
**last_issue** | [**Issue**](Issue.md) |  | [optional] 
**locations** | **list[object]** | List of locations that appeared in this volume. | [optional] 
**objects** | **list[object]** | List of objects that appeared in this volume. | [optional] 
**people** | **list[object]** | List of people that worked on this volume. | [optional] 
**publisher** | **object** | The primary publisher a volume is attached to. | [optional] 
**start_year** | **str** | The first year this volume appeared in comics. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


