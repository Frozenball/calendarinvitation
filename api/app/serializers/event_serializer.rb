class EventSerializer < ActiveModel::Serializer
  attributes :name, :start, :end, :location, :description, :slug
end
