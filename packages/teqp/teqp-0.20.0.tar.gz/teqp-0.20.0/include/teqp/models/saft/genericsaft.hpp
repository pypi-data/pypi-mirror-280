#pragma once

#include "teqp/models/pcsaft.hpp"
#include "teqp/models/saftvrmie.hpp"
#include "teqp/models/association/association.hpp"
#include "teqp/models/saft/softsaft.hpp"

namespace teqp::saft::genericsaft{

struct GenericSAFT{
    
public:
    using NonPolarTerms = std::variant<saft::pcsaft::PCSAFTMixture, SAFTVRMie::SAFTVRMieNonpolarMixture, saft::softsaft::SoftSAFT>;
//    using PolarTerms = EOSTermContainer<>;
    using AssociationTerms = std::variant<association::Association>;
    
private:
    auto make_nonpolar(const nlohmann::json &j) -> NonPolarTerms{
        std::string kind = j.at("kind");
        if (kind == "PCSAFT" || kind == "PC-SAFT"){
            return saft::pcsaft::PCSAFTfactory(j.at("model"));
        }
        else if (kind == "SAFTVRMie" || kind == "SAFT-VR-Mie"){
            return SAFTVRMie::SAFTVRMieNonpolarfactory(j.at("model"));
        }
        else if (kind == "Johnson+Johnson" || kind == "softSAFT"){
            return saft::softsaft::SoftSAFT(j.at("model"));
        }
        // TODO: 2CLJ
        else{
            throw std::invalid_argument("Not valid nonpolar kind:" + kind);
        }
    };
    auto make_association(const nlohmann::json &j) -> AssociationTerms{
        std::string kind = j.at("kind");
        if (kind == "canonical"){
            return association::Association(j.at("model"));
        }
        // TODO: Add the new Dufal association term
//        else if (kind == "Dufal-Mie"){
//            return std::make_unique<association::DufalMie>(j.at("model"));
//        }
        else{
            throw std::invalid_argument("Not valid association kind:" + kind);
        }
    };
    
public:
    GenericSAFT(const nlohmann::json&j) : nonpolar(make_nonpolar(j.at("nonpolar"))){
        if (j.contains("association")){
            association.emplace(make_association(j.at("association")));
        }
    }
    
    template<class VecType>
    auto R(const VecType& molefrac) const {
        return get_R_gas<decltype(molefrac[0])>();
    }
    
    NonPolarTerms nonpolar;
//    std::optional<PolarTerms> polar;
    std::optional<AssociationTerms> association;
    
    template <typename TType, typename RhoType, typename MoleFractions>
    auto alphar(const TType& T, const RhoType& rho, const MoleFractions& molefrac) const {
        auto contrib = std::visit([&](auto& t) { return t.alphar(T, rho, molefrac); }, nonpolar);
        if (association){
            const AssociationTerms& at = association.value();
            contrib += std::visit([&](auto& t) { return t.alphar(T, rho, molefrac); }, at);
        }
        return contrib;
    }
};

}
