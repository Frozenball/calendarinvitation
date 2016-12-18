class EventsController < ApplicationController
    respond_to :json
    # wrap_parameters format: [:json]

    def create
        puts request.raw_post
        puts params
        respond_with Event.create(
            name: params[:name],
            start: params[:start],
            end: params[:end],
            ip: request.env['REMOTE_ADDR'],
            location: params[:location],
            description: params[:description],
            secret: (0...4).map { (65 + rand(26)).chr }.join
        )
    end
    def show
        @event = Event.friendly.find(params[:id])
        puts @event.friendly_id
        render json: @event
    end
end
